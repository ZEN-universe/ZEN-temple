import os
from typing import Any, Optional

import numpy as np
import pandas as pd
from fastapi import HTTPException
from zen_garden.default_config import Analysis  # type: ignore
from zen_garden.postprocess.results import Results  # type: ignore

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
        scenario_name: Optional[str] = None,
        carrier: Optional[str] = None,
        node: Optional[str] = None,
        year: Optional[int] = None,
        rolling_average_window_size: int = 1,
    ) -> None:
        self.solution_name = solution_name
        self.scenario_name = scenario_name
        self.carrier = carrier
        self.year = year
        self.rolling_average_window_size = rolling_average_window_size
        self.node = node
        self.reference_technologies: Optional[list[str]] = None

        path = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
        if not os.path.exists(path) or not os.path.isdir(path):
            raise HTTPException(
                status_code=404, detail=f"Solution {solution_name} not found"
            )
        self.results = Results(path, enable_cache=False)

    def get_unit(self, component: str) -> str:
        """
        Returns the unit of a component for the current solution.
        If there are several units in the requested component, it returns it in form of a CSV string.

        :param component: Name of the component.
        """
        unit = self.results.get_unit(component, convert_to_yearly_unit=True)
        if type(unit) is str:
            unit = pd.DataFrame({0: [unit]})
        return self.__dataframe_to_csv(unit)

    def get_total(self, component: str) -> Optional[str]:
        """
        Returns the total and the unit of a component for the current solution.

        :param component: Name of the component.
        """
        # Build index for filtering by carrier if specified
        index = self.__build_index_for_carrier_and_node(component)

        # Get total
        total: pd.DataFrame | pd.Series[Any] = self.results.get_total(
            component, scenario_name=self.scenario_name, index=index
        )

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
        full_ts = self.results.get_full_ts(
            component, scenario_name=self.scenario_name, year=self.year, index=index
        )
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
        flow_transport = self.results.get_full_ts(
            "flow_transport",
            scenario_name=self.scenario_name,
            year=self.year,
            index=index,
        )
        flow_transport_loss = self.results.get_full_ts(
            "flow_transport_loss",
            scenario_name=self.scenario_name,
            year=self.year,
            index=index,
        )
        if flow_transport.empty:
            return [], []

        # Compute transport out: all transport flows going out the of the node
        transport_out = self.__filter_by_edges(flow_transport, "out")
        transport_out = transport_out.multiply(-1)
        transport_out = self.__compute_rolling_average(transport_out)
        transport_out = self.__quantify_response(transport_out)

        # Compute transport in: all transport flows going into the node minus the transport losses
        if not flow_transport_loss.empty:
            transport_in = flow_transport - flow_transport_loss
            transport_in = self.__filter_by_edges(transport_in, "in")
            transport_in = self.__compute_rolling_average(transport_in)
            transport_in = self.__quantify_response(transport_in)
        else:
            transport_in = []

        return transport_in, transport_out

    def get_dual(self, component: str) -> list[dict[str, Any]]:
        """
        Returns the dual values for a given component.

        :param component: Name of the component.
        """
        # Build index for filtering by carrier and node
        index = self.__build_index_for_carrier_and_node(component)

        # Get dual dataframe
        dual = self.results.get_dual(
            component, self.scenario_name, self.year, index=index
        )
        if dual is None:
            return []

        # Filter and quantify response
        dual = self.__skip_irrelevant_rows(dual)
        return self.__quantify_response(dual)

    def set_earliest_year_of_data(self):
        """
        Sets the earliest year of data for the current scenario to the earliest year available in the results.
        """
        earliest_year = self.results.get_analysis(
            self.scenario_name
        ).earliest_year_of_data
        if earliest_year is not None:
            self.year = int(earliest_year)

    def get_scenario_names(self) -> list[str]:
        """
        Returns the list of available scenarios for the current solution.
        """
        return list(self.results.solution_loader.scenarios.keys())

    def __skip_irrelevant_rows(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Filter out rows that are either duplicates or only contain zeros (up to a certain epsilon) in all columns.

        :param df: The dataframe to filter.
        """
        # Drop duplicates
        df = df.drop_duplicates()
        # Drop variables that only contain zeros
        df = df.loc[(abs(df) > config.EPS * max(df)).any(axis=1)]
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
        edges = self.results.get_df("set_nodes_on_edges", self.scenario_name)
        edges = [
            edge for edge, nodes in edges.items() if nodes.split(",")[idx] == self.node
        ]
        return df.loc[(slice(None), edges), :]

    def __build_index_for_carrier_and_node(
        self, component: str
    ) -> Optional[dict[str, str | list[str]]]:
        """
        Builds an index for filtering by carrier if specified.

        :param component: Name of the component.
        """
        if self.carrier is None and self.node is None:
            return None

        index_names = self.results.get_index_names(component, self.scenario_name)
        index = {}

        if self.node is not None and "node" in index_names:
            index["node"] = self.node
        elif self.node is not None:
            print(
                f"Warning: Cannot filter by node {self.node}: no 'node' index level for component {component} found.",
            )

        if self.carrier is not None and "carrier" in index_names:
            index["carrier"] = self.carrier
        elif self.carrier is not None and "technology" in index_names:
            reference_technologies = self.__get_reference_technologies()
            index["technology"] = reference_technologies
        elif self.carrier is not None:
            print(
                f"Warning: Cannot filter by carrier {self.carrier}: no 'carrier' or 'technology' index level for component {component} found."
            )

        return index

    def __get_reference_technologies(self) -> list[str]:
        """
        Returns the list of reference technologies for the current carrier.
        """
        if self.carrier is None:
            return []

        if self.reference_technologies is not None:
            return self.reference_technologies

        reference_carriers = self.results.get_df(
            "set_reference_carriers", scenario_name=self.scenario_name
        )
        reference_technologies = reference_carriers[
            reference_carriers == self.carrier
        ].index.tolist()

        # Ensure the result is always a list of strings
        reference_technologies_str = [str(tech) for tech in reference_technologies]
        self.reference_technologies = reference_technologies_str
        return reference_technologies_str

    def __compute_rolling_average(
        self, df: "pd.DataFrame | pd.Series[Any]"
    ) -> "pd.DataFrame | pd.Series[Any]":
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
