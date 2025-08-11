import os
from functools import cache
from os import walk
from typing import Any, Optional

import pandas as pd
from fastapi import HTTPException
from zen_garden.postprocess.results import Results  # type: ignore

from zen_temple.utils import get_variable_name

from ..config import config
from ..models.solution import (
    DataResult,
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
        return Results(path)

    def get_list(self) -> list[SolutionList]:
        """
        Creates a list of Solution-objects of all solutions that are contained in any folder contained in the configured SOLUTION_FOLDER.

        This function is very forgiving, it tries to instanciate a Solution for all folders in SOLUTION_FOLDER that contain a 'scenarios.json' file.
        If this fails, it skips the folder.
        """
        solutions_folders: set[str] = set()
        ans = []
        # TODO this is bad because if you accidently have a scenarios.json in a subscenario folder, it will be included in the list. Better check if parent folder is a solution (has scenarios.json)
        for dirpath, dirnames, filenames in walk(config.SOLUTION_FOLDER):
            if "scenarios.json" in filenames:
                solutions_folders.add(dirpath)
                # Prevent os.walk from going deeper into this folder
                dirnames.clear()
        for folder in solutions_folders:
            try:
                ans.append(SolutionList.from_path(folder))
            except (FileNotFoundError, NotADirectoryError) as e:
                print(str(e) + f" - Skip {folder}")
                continue
        return ans

    @cache
    def get_detail(self, solution_name: str) -> SolutionDetail:
        """
        Returns the SolutionDetail of a solution given its name.

        The solution name can contain dots which are treated as folders.
        So for example foo/bar.solution will resolve to the solition contained in foo/bar/solution, relative to
        the SOLUTION_FOLDER config value.

        :param solution_name: Name of the solution
        """
        path = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
        return SolutionDetail.from_path(path)

    @cache
    def get_full_ts(
        self,
        solution_name: str,
        component: str,
        scenario: Optional[str] = None,
        year: Optional[int] = None,
        rolling_average_window_size: int = 1,
    ) -> DataResult:
        """
        Returns the full ts and the unit of a component given the solution name, the component name and the scenario name.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        :param component: Name of the component.
        :param scenario: Name of the scenario. If skipped, the first scenario is taken.
        :param year: The year of the ts. If skipped, the first year is taken.
        """
        results = self.__load_results(solution_name)
        unit = self.__read_out_units(results, component)

        if year is None:
            year = 0

        full_ts = results.get_full_ts(component, scenario_name=scenario, year=year)
        data_csv = self.__process_full_ts(full_ts, rolling_average_window_size)

        return DataResult(data_csv=data_csv, unit=unit)

    def __process_full_ts(
        self,
        full_ts: Any,
        rolling_average_window_size: int = 1,
    ) -> str:
        if full_ts.shape[0] == 0:
            return ""

        full_ts = full_ts[~full_ts.index.duplicated(keep="first")]
        full_ts = full_ts.loc[(abs(full_ts) > config.EPS * max(full_ts)).any(axis=1)]

        if rolling_average_window_size > 1:
            full_ts = full_ts.rolling(rolling_average_window_size, axis=1).mean()

        return str(full_ts.to_csv(lineterminator="\n"))

    @cache
    def get_total(
        self, solution_name: str, component: str, scenario: Optional[str] = None
    ) -> DataResult:
        """
        Returns the total and the unit of a component given the solution name, the scenario name and the component name.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        :param component: Name of the component.
        :param scenario: Name of the scenario. If skipped, the first scenario is taken.
        """
        results = self.__load_results(solution_name)
        unit = self.__read_out_units(results, component)
        try:
            total: pd.DataFrame | pd.Series[Any] = results.get_total(
                component, scenario_name=scenario
            )
        except KeyError:
            raise HTTPException(status_code=404, detail=f"{component} not found!")

        total = self.__convert_total_to_series(total)

        return DataResult(data_csv=str(total.to_csv(lineterminator="\n")), unit=unit)

    def __convert_total_to_series(
        self, total: "pd.DataFrame | pd.Series[Any]"
    ) -> "pd.Series[Any]":
        """
        Converts the total to a pandas Series.
        """
        if type(total) is not pd.Series:
            return total.loc[(abs(total) > config.EPS * max(total)).any(axis=1)]  # type: ignore[no-any-return]
        return total

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
            unit = results.get_unit(component)
            if type(unit) is str:
                unit = pd.DataFrame({0: [unit]})
            return str(unit.to_csv(lineterminator="\n"))
        except Exception as e:
            print(e)
            return None
        return None

    @cache
    def get_production(
        self,
        solution_name: str,
        scenario: Optional[str] = None,
    ) -> dict[str, Optional[str]]:
        """
        Returns the production data of a solution.
        It returns a dictionary with the unit and the data of the production.

        :param solution_name: Name of the solution.
        :param scenario: Name of the scenario. If skipped, the first scenario is taken.
        :return: A dictionary with the unit and the data of the production.
        """
        results = self.__load_results(solution_name)
        response = {"unit": self.__read_out_units(results, "demand")}

        components = [
            "flow_conversion_output",
            "flow_conversion_input",
            "flow_storage_discharge",
            "flow_storage_charge",
            "flow_import",
            "flow_export",
            "shed_demand",
            "demand",
        ]
        for component in components:
            try:
                total: pd.DataFrame | pd.Series[Any] = results.get_total(
                    get_variable_name(
                        component, results.get_analysis().zen_garden_version
                    ),
                    scenario_name=scenario,
                )
            except KeyError:
                raise HTTPException(status_code=404, detail=f"{component} not found!")

            total = self.__convert_total_to_series(total)
            response.update({component: str(total.to_csv(lineterminator="\n"))})

        return response

    @cache
    def get_costs(
        self,
        solution_name: str,
        scenario: Optional[str] = None,
    ) -> dict[str, Optional[str]]:
        """
        Returns the costs data of a solution.
        It returns a dictionary with the unit and the data of the costs.

        :param solution_name: Name of the solution.
        :param scenario: Name of the scenario. If skipped, the first scenario is taken.
        :return: A dictionary with the unit and the data of the costs.
        """
        results = self.__load_results(solution_name)
        response = {"unit": self.__read_out_units(results, "cost_capex_yearly")}

        components = [
            "cost_capex_yearly",
            "cost_opex_yearly",
            "cost_carbon_emissions_total",
            "cost_carrier",
            "cost_shed_demand",
        ]
        for component in components:
            try:
                total: pd.DataFrame | pd.Series[Any] = results.get_total(
                    get_variable_name(
                        component, results.get_analysis().zen_garden_version
                    ),
                    scenario_name=scenario,
                )
            except KeyError:
                raise HTTPException(status_code=404, detail=f"{component} not found!")

            total = self.__convert_total_to_series(total)
            response.update({component: str(total.to_csv(lineterminator="\n"))})

        return response

    @cache
    def get_energy_balance(
        self,
        solution_name: str,
        node: str,
        carrier: str,
        scenario: Optional[str] = None,
        year: Optional[int] = None,
        rolling_average_window_size: int = 1,
    ) -> dict[str, str]:
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
                current_col = balances[key]

                if current_col.shape[0] == 0:
                    continue

                # Append end of df to beginning
                current_col = current_col[
                    current_col.columns[-rolling_average_window_size:].to_list()
                    + current_col.columns.to_list()
                ]

                # Rename columns for proper rolling
                current_col.columns = range(current_col.shape[1])

                current_col = current_col.T
                current_col = (
                    current_col.rolling(rolling_average_window_size).mean().dropna().T
                )

                # Rename columns again so it starts at 0
                current_col.columns = range(current_col.shape[1])

                balances[key] = current_col

        ans = {key: val.to_csv(lineterminator="\n") for key, val in balances.items()}

        return ans

    @cache
    def get_storage(
        self,
        solution_name: str,
        scenario: Optional[str] = None,
        year: Optional[int] = None,
        rolling_average_window_size: int = 1,
    ) -> dict[str, Optional[str]]:
        """
        Returns the storage data of a solution.
        It returns a dictionary with the unit and the data of the storage.

        :param solution_name: Name of the solution.
        :param scenario: Name of the scenario. If skipped, the first scenario is taken.
        :return: A dictionary with the unit and the data of the storage.
        """
        results = self.__load_results(solution_name)
        response = {"unit": self.__read_out_units(results, "storage_level")}

        if year is None:
            year = 0

        components = [
            "storage_level",
            "flow_storage_charge",
            "flow_storage_discharge",
            "flow_storage_spillage",
            "flow_storage_inflow",
        ]
        for component in components:
            full_ts = results.get_full_ts(component, scenario_name=scenario, year=year)

            response.update(
                {
                    component: self.__process_full_ts(
                        full_ts, rolling_average_window_size
                    )
                }
            )

        return response


solution_repository = SolutionRepository()
