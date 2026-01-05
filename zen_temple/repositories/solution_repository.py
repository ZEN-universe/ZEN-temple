from fastapi import HTTPException
import numpy as np
import os
import pandas as pd
from typing import Any, Optional
from zen_garden.postprocess.results import Results  # type: ignore
from zen_garden.default_config import Analysis  # type: ignore

from ..config import config
from ..versions import get_variable_name


class SolutionRepository:
    """
    Repository for accessing solution data.
    This class provides methods to access various data related to a solution,
    such as units, totals, full time series, and energy balances.

    :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
    :param scenario_name: Name of the scenario. If skipped, the first scenario is taken.
    :param carrier: Name of the carrier to filter by. If skipped, no filtering is applied.
    """

    def __init__(
        self,
        solution_name: str,
        scenario_name: Optional[str] = None,
        carrier: Optional[str] = None,
    ) -> None:
        self.solution_name = solution_name
        self.scenario_name = scenario_name
        self.carrier = carrier
        self.reference_technologies: Optional[list[str]] = None

        path = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
        if not os.path.exists(path) or not os.path.isdir(path):
            raise HTTPException(
                status_code=404, detail=f"Solution {solution_name} not found"
            )
        self.results = Results(path, enable_cache=False)

    def get_unit(self, component: str) -> Optional[str]:
        """
        Returns the unit of a component for the current solution.
        If there are several units in the requested component, it returns it in form of a CSV string.

        :param component: Name of the component.
        """
        try:
            unit = self.results.get_unit(component, convert_to_yearly_unit=True)
            if type(unit) is str:
                unit = pd.DataFrame({0: [unit]})
            return self.__dataframe_to_csv(unit)
        except Exception as e:
            print(e)
            return None

    def get_total(self, component: str) -> Optional[str]:
        """
        Returns the total and the unit of a component for the current solution.

        :param component: Name of the component.
        """
        # Build index for filtering by carrier if specified
        index = self.__build_index_for_carrier(component)

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
        year: int,
        rolling_average_window_size: int,
    ) -> Optional[list[dict[str, Any]] | str]:
        """
        Returns the full ts and the unit of a component given the solution name, the component name and the scenario name.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        :param component: Name of the component.
        :param scenario: Name of the scenario. If skipped, the first scenario is taken.
        :param year: The year of the ts. If skipped, the first year is taken.
        """
        # Build index for filtering by carrier if specified
        index = self.__build_index_for_carrier(component)

        # Get full time series
        full_ts = self.results.get_full_ts(
            component, scenario_name=self.scenario_name, year=year, index=index
        )
        if full_ts.shape[0] == 0:
            return []

        # Skip irrelevant rows
        full_ts = full_ts[~full_ts.index.duplicated(keep="first")]
        full_ts = full_ts.loc[(abs(full_ts) > config.EPS * max(full_ts)).any(axis=1)]

        # Apply rolling average
        if rolling_average_window_size > 1:
            full_ts = self.__compute_rolling_average(
                full_ts, rolling_average_window_size
            )

        return self.__quantify_response(full_ts)

    def get_energy_balance(
        self,
        node: str,
        carrier: str,
        year: Optional[int] = None,
        rolling_average_window_size: int = 1,
    ) -> dict[str, list[dict[str, Any]]]:
        """
        Returns the energy balance dataframes of a solution.
        It drops duplicates of all dataframes and removes the variables that only contain zeros.

        :param node: The name of the node.
        :param carrier: The name of the carrier.
        :param year: The desired year. If skipped, the first year is taken.
        :param rolling_average_window_size: Size of the rolling average window.
        """
        if year is None:
            year = 0

        balances: dict[str, pd.DataFrame | pd.Series[Any]] = (
            self.results.get_energy_balance_dataframes(
                node, carrier, year, self.scenario_name
            )
        )

        # Add dual of energy balance constraint
        duals = self.results.get_dual(
            "constraint_nodal_energy_balance",
            scenario_name=self.scenario_name,
            year=year,
        )
        if duals is not None:
            balances["constraint_nodal_energy_balance"] = duals.xs(
                (carrier, node), level=("carrier", "node")
            )
        else:
            balances["constraint_nodal_energy_balance"] = pd.Series(dtype=float)

        # Drop duplicates of all dataframes
        balances = {
            key: val[~val.index.duplicated(keep="first")]
            for key, val in balances.items()
        }

        # Drop variables that only contain zeros (except for demand)
        demand_name = get_variable_name(
            "demand", self.results.get_analysis().zen_garden_version
        )
        for key, series in balances.items():
            if type(series) is not pd.Series and key != demand_name:
                if series.empty:
                    continue
                balances[key] = series.loc[
                    (abs(series) > config.EPS * max(series)).any(axis=1)
                ]

            if rolling_average_window_size > 1:
                balances[key] = self.__compute_rolling_average(
                    balances[key], rolling_average_window_size
                )

        # Quantify all dataframes
        ans = {key: self.__quantify_response(val) for key, val in balances.items()}

        return ans

    def get_analysis(self) -> Analysis:
        """
        Returns the analysis object for the current scenario.
        """
        return self.results.get_analysis(self.scenario_name)

    def get_scenario_names(self) -> list[str]:
        """
        Returns the list of available scenarios for the current solution.
        """
        return list(self.results.solution_loader.scenarios.keys())

    def __build_index_for_carrier(
        self, component: str
    ) -> Optional[dict[str, str | list[str]]]:
        """
        Builds an index for filtering by carrier if specified.

        :param component: Name of the component.
        """
        if self.carrier is None:
            return None

        index_names = self.results.get_index_names(component, self.scenario_name)

        if "carrier" in index_names:
            return {"carrier": self.carrier}

        if "technology" in index_names:
            reference_technologies = self.__get_reference_technologies()
            return {"technology": reference_technologies}

        print(
            "Warning: Cannot filter by carrier, no 'carrier' or 'technology' index level found."
        )
        return None

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
        self, df: "pd.DataFrame | pd.Series[Any]", window_size: int
    ) -> "pd.DataFrame | pd.Series[Any]":
        """
        Computes the rolling average of a DataFrame or Series with wrap-around.

        :param df: The DataFrame or Series to compute the rolling average of.
        :param window_size: The size of the rolling average window.
        """
        if df.shape[0] == 0:
            return df

        # Append end of df to beginning
        df = df[df.columns[-window_size + 1 :].to_list() + df.columns.to_list()]

        # Compute rolling average
        df = df.T.rolling(window_size).mean().dropna().T

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
