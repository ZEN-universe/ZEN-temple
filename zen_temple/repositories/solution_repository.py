import os
from functools import cache
from os import walk
from typing import Any, Optional

import pandas as pd
import numpy as np
from fastapi import HTTPException
from zen_garden.postprocess.results import Results  # type: ignore

from zen_temple.errors import InvalidSolutionFolderError
from zen_temple.utils import get_variable_name

from ..config import config
from ..models.solution import (
    SolutionDetail,
    SolutionList,
)


class SolutionRepository:
    def __load_results(self, solution_name: str) -> Results:
        """
        Loads the results of a solution given its name.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        :return: Results object of the solution.
        """
        path = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
        if not os.path.exists(path) or not os.path.isdir(path):
            raise HTTPException(
                status_code=404, detail=f"Solution {solution_name} not found"
            )
        return Results(path)

    def __dataframe_to_csv(self, df: "pd.DataFrame | pd.Series[Any]") -> str:
        """
        Converts a DataFrame or Series to a CSV string.
        """
        return df.to_csv(
            lineterminator="\n",
            float_format=f"%.{config.RESPONSE_SIGNIFICANT_DIGITS}g",
        )

    def get_list(self) -> list[SolutionList]:
        """
        Creates a list of Solution-objects of all solutions that are contained in any folder contained in the configured SOLUTION_FOLDER.

        This function is very forgiving, it tries to instantiate a solution for all folders in SOLUTION_FOLDER that contain a 'scenarios.json' file.
        If this fails, it skips the folder.
        """
        solutions_folders: set[str] = set()
        ans = []
        # TODO this is bad because if you accidentally have a scenarios.json in a subscenario folder, it will be included in the list.
        #      Better check if the parent folder is a solution, i.e., whether is has a scenarios.json
        for dirpath, dirnames, filenames in walk(config.SOLUTION_FOLDER):
            if "scenarios.json" in filenames:
                solutions_folders.add(dirpath)
                # Prevent os.walk from going deeper into this folder
                dirnames.clear()
        for folder in solutions_folders:
            try:
                ans.append(SolutionList.from_path(folder))
            except (
                FileNotFoundError,
                NotADirectoryError,
                InvalidSolutionFolderError,
            ) as e:
                print(str(e) + f" - Skip {folder}")
                continue
        return ans

    @cache
    def get_detail(self, solution_name: str) -> SolutionDetail:
        """
        Returns the SolutionDetail of a solution given its name.

        The solution name can contain dots which are treated as folders.
        So for example foo/bar.solution will resolve to the solution contained in foo/bar/solution, relative to
        the SOLUTION_FOLDER config value.

        :param solution_name: Name of the solution
        """
        path = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
        return SolutionDetail.from_path(path)

    @cache
    def get_full_ts(
        self,
        solution_name: str,
        components_str: str,
        unit_component: Optional[str] = None,
        scenario: Optional[str] = None,
        year: Optional[int] = None,
        rolling_average_window_size: int = 1,
    ) -> dict[str, Optional[list[dict[str, Any]] | str]]:
        """
        Returns the full ts and the unit of a component given the solution name, the component name and the scenario name.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        :param component: Name of the component.
        :param scenario: Name of the scenario. If skipped, the first scenario is taken.
        :param year: The year of the ts. If skipped, the first year is taken.
        """
        components = [x for x in components_str.split(",") if x != ""]
        if len(components) == 0:
            raise HTTPException(status_code=400, detail="No components provided!")

        results = self.__load_results(solution_name)
        unit = self.__read_out_units(
            results,
            (
                unit_component
                if unit_component and unit_component is not None
                else components[0]
            ),
        )
        response: dict[str, Optional[list[dict[str, Any]] | str]] = {"unit": unit}

        if year is None:
            year = results.get_analysis(scenario).earliest_year_of_data

        for component in components:
            full_ts = results.get_full_ts(component, scenario_name=scenario, year=year)
            if full_ts.shape[0] == 0:
                response.update({component: []})
                continue

            full_ts = full_ts[~full_ts.index.duplicated(keep="first")]
            full_ts = full_ts.loc[
                (abs(full_ts) > config.EPS * max(full_ts)).any(axis=1)
            ]

            if rolling_average_window_size > 1:
                full_ts = self.__compute_rolling_average(
                    full_ts, rolling_average_window_size
                )

            res = self.__quantify_response(full_ts)
            response[component] = res

        return response

    def __compute_rolling_average(
        self, df: "pd.DataFrame | pd.Series[Any]", window_size: int
    ) -> "pd.DataFrame | pd.Series[Any]":
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

    @cache
    def get_total(
        self,
        solution_name: str,
        components_str: str,
        unit_component: Optional[str] = None,
        scenario: Optional[str] = None,
    ) -> dict[str, Optional[str]]:
        """
        Returns the total and the unit of a component given the solution name, the scenario name and the component name.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        :param component: Name of the component.
        :param scenario: Name of the scenario. If skipped, the first scenario is taken.
        """
        components = [x for x in components_str.split(",") if x != ""]
        if len(components) == 0:
            raise HTTPException(status_code=400, detail="No components provided!")

        results = self.__load_results(solution_name)
        unit = self.__read_out_units(
            results,
            (
                unit_component
                if unit_component and unit_component is not None
                else components[0]
            ),
        )
        response = {"unit": unit}

        for component in components:
            try:
                total: pd.DataFrame | pd.Series[Any] = results.get_total(
                    component, scenario_name=scenario
                )
            except KeyError:
                raise HTTPException(
                    status_code=404, detail=f"{component} not found in {solution_name}"
                )

            # Skip irrelevant rows in dataframes
            if type(total) is not pd.Series:
                total = total.loc[(abs(total) > config.EPS * max(total)).any(axis=1)]
            response.update({component: self.__dataframe_to_csv(total)})

        return response

    def get_unit(self, solution_name: str, component: str) -> Optional[str]:
        """
        Returns the unit of a component given the solution name. If there are several units in the requested component, it returns it in form of a CSV string.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        """
        return self.__read_out_units(self.__load_results(solution_name), component)

    def __read_out_units(self, results: Results, component: str) -> Optional[str]:
        """
        Reads out the units of a component from the results object.
        """
        try:
            unit = results.get_unit(component, convert_to_yearly_unit=True)
            if type(unit) is str:
                unit = pd.DataFrame({0: [unit]})
            return self.__dataframe_to_csv(unit)
        except Exception as e:
            print(e)
            return None

    @cache
    def get_energy_balance(
        self,
        solution_name: str,
        node: str,
        carrier: str,
        scenario: Optional[str] = None,
        year: Optional[int] = None,
        rolling_average_window_size: int = 1,
    ) -> dict[str, list[dict[str, Any]]]:
        """
        Returns the energy balance dataframes of a solution.
        It drops duplicates of all dataframes and removes the variables that only contain zeros.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        :param node: The name of the node.
        :param carrier: The name of the carrier.
        :param scenario: The name of the scenario. If skipped, the first scenario is taken.
        :param year: The desired year. If skipped, the first year is taken.
        :param rolling_average_window_size: Size of the rolling average window.
        """
        results = self.__load_results(solution_name)

        if year is None:
            year = 0

        balances: dict[str, pd.DataFrame | pd.Series[Any]] = (
            results.get_energy_balance_dataframes(node, carrier, year, scenario)
        )

        # Add dual of energy balance constraint
        duals = results.get_dual(
            "constraint_nodal_energy_balance", scenario_name=scenario, year=year
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
        for key, series in balances.items():
            demand_name = get_variable_name(
                "demand", results.get_analysis().zen_garden_version
            )

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


solution_repository = SolutionRepository()
