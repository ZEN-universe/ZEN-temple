import os
from functools import cache
from os import walk
from typing import Any, Optional

import pandas as pd
from fastapi import HTTPException
from zen_garden.postprocess.results import Results  # type: ignore
from time import perf_counter
from ..config import config
from ..models.solution import (
    DataResult,
    SolutionDetail,
    SolutionList,
)


class SolutionRepository:
    def get_list(self) -> list[SolutionList]:
        """
        Creates a list of Solution-objects of all solutions that are contained in any folder contained in the configured SOLUTION_FOLDER.

        This function is very forgiving, it tries to instanciate a Solution for all folders in SOLUTION_FOLDER that contain a 'scenarios.json' file.
        If this fails, it skips the folder.
        """
        solutions_folders: set[str] = set()
        ans = []
        for dirpath, _, filenames in walk(config.SOLUTION_FOLDER):
            if "scenarios.json" in filenames:
                solutions_folders.add(dirpath)

        for folder in solutions_folders:
            try:
                ans.append(SolutionList.from_path(folder))
            except (FileNotFoundError, NotADirectoryError):
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
    ) -> DataResult:
        """
        Returns the full ts and the unit of a component given the solution name, the component name and the scenario name.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        :param component: Name of the component.
        :param scenario: Name of the scenario. If skipped, the first scenario is taken.
        :param year: The year of the ts. If skipped, the first year is taken.
        """
        solution_folder = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
        unit = self.get_unit(solution_name, component)
        results = Results(solution_folder)

        if year is None:
            year = 0

        full_ts = results.get_full_ts(component, scenario_name=scenario, year=year)
        full_ts = full_ts[~full_ts.index.duplicated(keep="first")]
        full_ts = full_ts.loc[~(full_ts == 0).all(axis=1)]

        return DataResult(data_csv=str(full_ts.to_csv()), unit=unit)

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
        solution_folder = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
        results = Results(solution_folder)
        unit = self.get_unit(solution_name, component)
        try:
            total: pd.DataFrame | pd.Series[Any] = results.get_total(
                component, scenario_name=scenario
            )
        except KeyError:
            raise HTTPException(status_code=404, detail=f"{component} not found!")

        if type(total) is not pd.Series:
            total = total.loc[~(total == 0).all(axis=1)]

        return DataResult(data_csv=str(total.to_csv()), unit=unit)

    def get_unit(self, solution_name: str, component: str) -> Optional[str]:
        """
        Returns the unit of a component given the solution name. If there are several units in the requested component, it returns it in form of a CSV string.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        """
        solution_folder = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
        results = Results(solution_folder)

        unit_str: str | None = None
        try:
            unit: str | pd.DataFrame = results.get_unit(component)
            if type(unit) is str:
                unit = pd.DataFrame({0: [unit]})
            unit_str = str(unit.to_csv())  # type: ignore

        except Exception:
            unit_str = None
        return unit_str

    @cache
    def get_energy_balance(
        self,
        solution_name: str,
        node: str,
        carrier: str,
        scenario: Optional[str] = None,
        year: Optional[int] = None,
    ) -> dict[str, str]:
        """
        Returns the energy balance dataframes of a solution.
        It drops duplicates of all dataframes and removes the variables that only contain zeros.

        :param solution_name: Name of the solution. Dots will be regarded as subfolders (foo.bar => foo/bar).
        :param node: The name of the node.
        :param carrier: The name of the carrier.
        :param scenario: The name of the scenario. If skipped, the first scenario is taken.
        :param year: The desired year. If skipped, the first year is taken.
        """
        solution_folder = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
        results = Results(solution_folder)

        if year is None:
            year = 0

        balances: dict[str, pd.DataFrame | pd.Series[Any]] = (
            results.get_energy_balance_dataframes(node, carrier, year, scenario)
        )

        # Drop duplicates of all dataframes
        balances = {
            key: val[~val.index.duplicated(keep="first")] for key, val in balances.items()
        }

        # Drop variables that only contain zeros (except for demand)
        for key, series in balances.items():
            if key == "demand":
                continue

            if type(series) is not pd.Series:
                balances[key] = series.loc[~(series == 0).all(axis=1)]  # type: ignore

        ans = {key: val.to_csv() for key, val in balances.items()}

        return ans


solution_repository = SolutionRepository()
