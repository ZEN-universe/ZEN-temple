import os
from typing import Any

import numpy as np
import pandas as pd
from fastapi import HTTPException
from zen_garden.postprocess.results import Results  # type: ignore
from zen_garden.postprocess.results.scenario import (  # type: ignore
    Scenario,
)

from ..config import config


class SolutionRepository:
    """
    Repository for accessing solution data.
    This class provides methods to access various data related to a solution,
    such as units, totals, full time series, and energy balances.

    :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
    :param scenario_name: Name of the scenario. If skipped, the first scenario is taken.
    :param carrier: Name of the carrier to filter by. If skipped, no filtering is applied.
    :param node: Name of the node to filter by. If skipped, no filtering is applied.
    :param year: The year of the time series. If skipped, the first year is taken.
    :param rolling_average_window_size: Size of the rolling average window. If skipped, no rolling average is applied.
    """

    def __init__(
        self,
        solution_name: str,
        scenario_name: str | None = None,
        carrier: str | None = None,
        node: str | None = None,
        year: int | None = None,
        rolling_average_window_size: int = 1,
    ) -> None:
        self.solution_name: str = solution_name
        self.scenario_name: str | None = scenario_name
        self.carrier: str | None = carrier
        self.year: int | None = year
        self.rolling_average_window_size: int = rolling_average_window_size
        self.node: str | None = node
        self.reference_technologies: list[str] | None = None

        path = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
        if not os.path.exists(path) or not os.path.isdir(path):
            raise HTTPException(
                status_code=404, detail=f"Solution {solution_name} not found"
            )
        self.results: Results = Results(path)
        self.scenario: Scenario = (
            self.results.scenarios[scenario_name]
            if scenario_name is not None
            else self.results.first_scenario
        )

    def get_unit(self, component: str) -> str:
        """
        Returns the unit of a component for the current solution.
        If there are several units in the requested component, it returns it in form of a CSV string.

        :param component: Name of the component.
        """
        unit = self.scenario.get_unit(component, convert_to_yearly_unit=True)
        if type(unit) is str:
            unit = pd.DataFrame({0: [unit]})
        return self.__dataframe_to_csv(unit)

    def get_total(self, component: str) -> str | None:
        """
        Returns the total and the unit of a component for the current solution.

        :param component: Name of the component.
        """
        # Build index for filtering by carrier if specified
        index = self.__build_index_for_carrier_and_node(component)

        # Get total
        total = self.scenario.get_total(component, index=index)

        # Skip irrelevant rows in dataframes
        if type(total) is not pd.Series and not total.empty:
            total = total.loc[(abs(total) > config.EPS * max(total)).any(axis=1)]

        return self.__dataframe_to_csv(total)

    def get_full_ts(
        self,
        component: str,
        factor: int = 1,
    ) -> list[dict[str, Any]]:
        """
        Returns the full ts and the unit of a component given the solution name, the component name and the scenario name.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        :param component: Name of the component.
        :param factor: Factor to multiply the values with. If skipped, no multiplication is applied.
        """
        # Build index for filtering by carrier if specified
        index = self.__build_index_for_carrier_and_node(component)

        # Get full time series
        full_ts = self.scenario.get_full_ts(component, year=self.year, index=index)
        if full_ts.shape[0] == 0:
            return []

        full_ts = self.__skip_irrelevant_rows(full_ts)
        full_ts = full_ts * factor
        full_ts = self.__compute_rolling_average(full_ts)
        return self.__quantify_response(full_ts)

    def get_transport_flows(self) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        """
        Returns the transport flows in and out of a node for a given year and rolling average window size.
        The transport flows out of the node are negated, so that positive values always indicate an increase of the carrier at the node.
        The transport flows in the node are computed as the transport flows into the node minus the transport losses at the node, if available.
        """
        # Build index for filtering by carrier and node
        index = self.__build_index_for_carrier_and_node("flow_transport")

        # Get flow transport and flow transport loss dataframes
        flow_transport = self.scenario.get_full_ts(
            "flow_transport",
            year=self.year,
            index=index,
        )
        flow_transport_loss = self.scenario.get_full_ts(
            "flow_transport_loss",
            year=self.year,
            index=index,
        )
        if flow_transport.empty:
            return [], []

        # Compute transport out: all transport flows going out the of the node
        transport_out_df = self.__filter_by_edges(flow_transport, "out")
        transport_out_df = transport_out_df.multiply(-1)
        transport_out_df = self.__compute_rolling_average(transport_out_df)
        transport_out_response = self.__quantify_response(transport_out_df)

        # Compute transport in: all transport flows going into the node minus the transport losses
        if not flow_transport_loss.empty:
            transport_in_df = flow_transport - flow_transport_loss
            transport_in_df = self.__filter_by_edges(transport_in_df, "in")
            transport_in_df = self.__compute_rolling_average(transport_in_df)
            transport_in_response = self.__quantify_response(transport_in_df)
        else:
            transport_in_response = []

        return transport_in_response, transport_out_response

    def get_dual(self, component: str) -> list[dict[str, Any]]:
        """
        Returns the dual values for a given component.

        :param component: Name of the component.
        """
        if not self.scenario.solver.save_duals:
            return []

        # Build index for filtering by carrier and node
        index = self.__build_index_for_carrier_and_node(component)

        # Get dual dataframe
        dual = self.scenario.get_dual(component, self.year, index=index)
        if dual is None:
            return []

        # Filter and quantify response
        dual = self.__skip_irrelevant_rows(dual)
        return self.__quantify_response(dual)

    def set_earliest_year_of_data(self) -> None:
        """
        Sets the earliest year of data for the current scenario to the earliest year available in the results.
        """
        self.year = self.scenario.analysis.earliest_year_of_data

    def get_scenario_names(self) -> list[str]:
        """
        Returns the list of available scenarios for the current solution.
        """
        return list(self.results.scenarios.keys())

    def __skip_irrelevant_rows(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Filter out rows that are either duplicates or only contain zeros (up to a certain epsilon) in all columns.

        :param df: The dataframe to filter.
        """
        # Drop duplicates
        df = df.drop_duplicates()
        # Drop variables that only contain zeros
        max_values = df.max()
        df = df.loc[(abs(df) > config.EPS * max_values).any(axis=1)]
        return df

    def __filter_by_edges(self, df: pd.DataFrame, direction: str) -> pd.DataFrame:
        """
        Filters the given data by the edges columns for the given node and direction.

        :param df: The dataframe to filter. It is expected to have a MultiIndex
            with the second level containing the edge names.
        :param direction: The direction of the transport flow to filter by.
            It can be either "in" or "out". "in" will filter for edges where the node is the destination,
            while "out" will filter for edges where the node is the source.
        """
        if self.node is None:
            return df
        idx = 0 if direction == "out" else 1
        edges = self.scenario.get_values("set_nodes_on_edges")
        edges = [
            edge for edge, nodes in edges.items() if nodes.split(",")[idx] == self.node
        ]
        return df.loc[(slice(None), edges), :]

    def __build_index_for_carrier_and_node(self, component: str) -> dict[str, str] | None:
        """
        Builds an index for filtering by carrier if specified.

        :param component: Name of the component.
        """
        if self.carrier is None and self.node is None:
            return None

        index_names = self.scenario.get_index_names(component)
        index: dict[str, str] = {}

        if self.node is not None and "set_nodes" in index_names:
            index["set_nodes"] = f"set_nodes == {self.node!r}"
        elif self.node is not None:
            print(
                f"Warning: Cannot filter by node {self.node}: no 'node' index level for component {component} found.",
            )

        carrier_index_names = self._index_names_of_header("carrier") & set(index_names)
        technology_index_names = self._index_names_of_header("technology") & set(
            index_names
        )
        if self.carrier is not None and len(carrier_index_names) > 0:
            dim = carrier_index_names.pop()
            index[dim] = f"{dim} == {self.carrier!r}"
        elif self.carrier is not None and len(technology_index_names) > 0:
            dim = technology_index_names.pop()
            reference_technologies = self.__get_reference_technologies()
            index[dim] = f"{dim} in {reference_technologies!r}"
        elif self.carrier is not None:
            print(
                f"Warning: Cannot filter by carrier {self.carrier}: no 'carrier' or 'technology' index level for component {component} found."
            )

        return index

    def _index_names_of_header(self, header: str) -> set[str]:
        """Returns the index names that belong to the given header.

        :param header: Name of the header.
        :return List of index names that map to the given header name.
        """
        return set(
            [
                key
                for key, value in self.scenario.analysis.header_data_inputs.items()
                if value == header
            ]
        )

    def __get_reference_technologies(self) -> list[str]:
        """
        Returns the list of reference technologies for the current carrier.
        """
        if self.carrier is None:
            return []

        if self.reference_technologies is not None:
            return self.reference_technologies

        reference_carriers = self.scenario.get_values("set_reference_carriers")
        reference_technologies = reference_carriers[
            reference_carriers == self.carrier
        ].index.tolist()

        # Ensure the result is always a list of strings
        reference_technologies_str = [str(tech) for tech in reference_technologies]
        self.reference_technologies = reference_technologies_str
        return reference_technologies_str

    def __compute_rolling_average(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Computes the rolling average of a DataFrame or Series with wrap-around.

        :param df: The DataFrame or Series to compute the rolling average of.
        :param window_size: The size of the rolling average window.
        """
        if df.shape[0] == 0 or self.rolling_average_window_size <= 1:
            return df

        # Append end of df to beginning
        df = df[
            df.columns[-self.rolling_average_window_size + 1 :].to_list()
            + df.columns.to_list()
        ]

        # Compute rolling average
        df = df.T.rolling(self.rolling_average_window_size).mean().dropna().T

        # Rename columns so it starts at 0
        df = df.set_axis(range(df.shape[1]), axis=1)

        return df

    def __quantify_response(self, df: "Any") -> list[dict[str, Any]]:
        """
        Converts a DataFrame or Series to a dictionary with quantized values.
        Quantization is done by mapping the values of each row to the interval [0, quantile),
        converting them to integers and delta encode them.

        The response contains the transformation parameters `(translation, scale)`
        such that we can reverse this process using:

        ```
        values = np.cumsum(values)
        values = values * scale + translation
        ```

        This design is analogous to TopoJSON's quantization scheme.
        """
        if df.shape[0] == 0:
            return []

        # Get index and data values
        index_names = df.index.names
        index_values = df.index.to_numpy()
        data_values = df.to_numpy()

        # Compute min/max per row
        min_values = data_values.min(axis=1)
        max_values = data_values.max(axis=1)
        diff_values = max_values - min_values

        # Compute translation and scale parameters for mapping the value to [0, quantile)
        translations = min_values
        quantile = 10 ** (config.RESPONSE_SIGNIFICANT_DIGITS)
        scales = (diff_values + config.EPS) / (quantile - 1)

        # Apply translation and scaling
        data_values = (data_values - translations[:, None]) / scales[:, None]

        # Convert to int
        data_values = data_values.astype(int)

        # Delta encode values
        data_values = np.diff(data_values, prepend=0)

        return [
            {
                **dict(zip(index_names, idx)),
                "d": row.tolist(),
                "t": (translation, scale),
            }
            for idx, row, translation, scale in zip(
                index_values, data_values, translations, scales
            )
        ]

    def __dataframe_to_csv(self, df: "pd.DataFrame | pd.Series[Any]") -> str:
        """
        Converts a DataFrame or Series to a CSV string.
        """
        if df.empty:
            return ""
        return df.to_csv(
            lineterminator="\n",
            float_format=f"%.{config.RESPONSE_SIGNIFICANT_DIGITS}g",
        )
