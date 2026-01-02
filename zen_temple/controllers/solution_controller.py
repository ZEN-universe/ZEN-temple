from fastapi import HTTPException
from functools import lru_cache
import os
from typing import Any, Optional

from ..config import config
from ..errors import InvalidSolutionFolderError
from ..models.solution_detail import SolutionDetail
from ..models.solution_list import SolutionList
from ..repositories.solution_repository import SolutionRepository


def verify_scenario_name(
    repository: SolutionRepository,
    solution_name: str,
    scenario_name: Optional[str],
) -> None:
    """
    Verifies that the provided scenario name exists in the solution repository.

    :param repository: The solution repository.
    :param solution_name: Name of the solution.
    :param scenario_name: Name of the scenario.

    :raises HTTPException: If the scenario name does not exist.
    """
    if scenario_name is None:
        return

    available_scenarios = repository.get_scenario_names()
    if scenario_name not in available_scenarios:
        scenario_names = ", ".join(available_scenarios)
        raise HTTPException(
            status_code=400,
            detail=f"Scenario '{scenario_name}' does not exist for solution '{solution_name}'. Available scenarios: {scenario_names}.",
        )


def get_list() -> list[SolutionList]:
    """
    Creates a list of `Solution`-objects of all solutions that are contained
    in any folder contained in the configured `SOLUTION_FOLDER`.

    This function is very forgiving, as it tries to instantiate a solution
    for all folders in `SOLUTION_FOLDER` that contain a `scenarios.json` file.
    If this fails, it skips the folder.
    """
    solutions_folders: set[str] = set()
    ans = []
    # TODO this is bad because if you accidentally have a scenarios.json in a subscenario folder, it will be included in the list.
    #      Better check if the parent folder is a solution, i.e., whether is has a scenarios.json
    for dirpath, dirnames, filenames in os.walk(config.SOLUTION_FOLDER):
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


@lru_cache(maxsize=128, typed=True)
def get_detail(solution_name: str) -> SolutionDetail:
    """
    Returns the `SolutionDetail` of a solution given its name.

    The solution name can contain dots which are treated as folders.
    So for example foo/bar.solution will resolve to the solution contained
    in foo/bar/solution, relative to the `SOLUTION_FOLDER` config value.

    :param solution_name: Name of the solution
    """
    path = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
    return SolutionDetail.from_path(path)


@lru_cache(maxsize=128, typed=True)
def get_unit(solution_name: str, component: str) -> Optional[str]:
    """
    Returns the unit of a component given the solution name.
    If there are several units in the requested component,
    it returns it in form of a CSV string.

    :param solution_name: Name of the solution.
        Dots will be regarded as subfolders (foo.bar => foo/bar).
    """
    return SolutionRepository(solution_name).get_unit(component)


@lru_cache(maxsize=32, typed=True)
def get_total(
    solution_name: str,
    components_str: str,
    unit_component: Optional[str] = None,
    scenario: Optional[str] = None,
    carrier: Optional[str] = None,
) -> dict[str, Optional[str]]:
    """
    Returns the total and the unit for a list of components.

    :param solution_name: Name of the solution.
        Dots will be regarded as subfolders (foo.bar => foo/bar).
    :param components_str: Names of the components, separated by commas.
    :param unit_component: Name of the component for which the unit is requested.
        If not provided, the first component in `components_str` is used.
    :param scenario: Name of the scenario. If skipped, the first scenario is taken.
    """
    components = [x for x in components_str.split(",") if x != ""]
    if len(components) == 0:
        raise HTTPException(status_code=400, detail="No components provided!")

    repository = SolutionRepository(solution_name, scenario, carrier)

    verify_scenario_name(repository, solution_name, scenario)

    if unit_component is None or unit_component == "":
        unit_component = components[0]

    unit = repository.get_unit(unit_component)
    response = {"unit": unit}

    for component in components:
        response[component] = repository.get_total(component)

    return response


@lru_cache(maxsize=16, typed=True)
def get_full_ts(
    solution_name: str,
    components_str: str,
    unit_component: Optional[str] = None,
    scenario_name: Optional[str] = None,
    year: Optional[int] = None,
    rolling_average_window_size: int = 1,
    carrier: Optional[str] = None,
) -> dict[str, Optional[list[dict[str, Any]] | str]]:
    """
    Returns the full ts and the unit for a list of components.

    :param solution_name: Name of the solution.
        Dots will be regarded as subfolders (foo.bar => foo/bar).
    :param components_str: Names of the components, separated by commas.
    :param unit_component: Name of the component for which the unit is requested.
        If not provided, the first component in `components_str` is used.
    :param scenario_name: Name of the scenario.
        If skipped, the first scenario is taken.
    :param year: The year of the ts. If skipped, the first year is taken.
    :param rolling_average_window_size: Size of the rolling average window.
    """
    components = [x for x in components_str.split(",") if x != ""]
    if len(components) == 0:
        raise HTTPException(status_code=400, detail="No components provided!")

    repository = SolutionRepository(solution_name, scenario_name, carrier)

    verify_scenario_name(repository, solution_name, scenario_name)

    if unit_component is None or unit_component == "":
        unit_component = components[0]

    unit = repository.get_unit(unit_component)
    response: dict[str, Optional[list[dict[str, Any]] | str]] = {"unit": unit}

    if year is None:
        year = repository.get_analysis().earliest_year_of_data

    for component in components:
        response[component] = repository.get_full_ts(
            component, year, rolling_average_window_size
        )

    return response


@lru_cache(maxsize=32, typed=True)
def get_energy_balance(
    solution_name: str,
    node: str,
    carrier: str,
    scenario_name: Optional[str] = None,
    year: Optional[int] = None,
    rolling_average_window_size: int = 1,
) -> dict[str, list[dict[str, Any]]]:
    """
    Returns the energy balance dataframes of a solution.
    It drops duplicates of all dataframes and removes the variables
    that only contain zeros.

    :param solution_name: Name of the solution.
        Dots will be regarded as subfolders (foo.bar => foo/bar).
    :param node: The name of the node.
    :param carrier: The name of the carrier.
    :param scenario_name: The name of the scenario.
        If skipped, the first scenario is taken.
    :param year: The desired year. If skipped, the first year is taken.
    :param rolling_average_window_size: Size of the rolling average window.
    """
    return SolutionRepository(solution_name, scenario_name).get_energy_balance(
        node, carrier, year, rolling_average_window_size
    )
