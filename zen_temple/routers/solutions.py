from typing import Any, Optional

from fastapi import Query, APIRouter

from ..models.solution import SolutionDetail, SolutionList
from ..repositories.solution_repository import solution_repository

router = APIRouter(prefix="/solutions", tags=["Solutions"])


@router.get("/list")
async def get_list() -> list[SolutionList]:
    """
    Get a list of the available solutions.
    """
    return solution_repository.get_list()


@router.get("/get_detail/{solution_name}")
async def get_detail(solution_name: str) -> SolutionDetail:
    """
    Get the details of a solution.
    """
    return solution_repository.get_detail(solution_name)


@router.get("/get_total")
async def get_total(
    solution_name: str,
    components: list[str] = Query(...),
    unit_component: Optional[str] = None,
    scenario: Optional[str] = None,
) -> dict[str, Optional[str]]:
    """
    Get the total of a variable given the solution name, the variable name, and the scenario. If no scenario is provided, the first scenarios in the list is taken.
    """
    return solution_repository.get_total(
        solution_name, ",".join(components), unit_component, scenario
    )


@router.get("/get_full_ts")
async def get_full_ts(
    solution_name: str,
    components: list[str] = Query(...),
    unit_component: Optional[str] = None,
    scenario: Optional[str] = None,
    year: Optional[int] = None,
    rolling_average_size: int = 1,
) -> dict[str, Optional[list[dict[str, Any]] | str]]:
    """
    Get the total of a variable given the solution name, the variable name, and the scenario. If no scenario is provided, the first scenarios in the list is taken.
    """
    return solution_repository.get_full_ts(
        solution_name,
        ",".join(components),
        unit_component,
        scenario,
        year,
        rolling_average_size,
    )


@router.get("/get_unit/{solution_name}/{variable_name}")
async def get_unit(solution_name: str, variable_name: str) -> Optional[str]:
    """
    Get the unit of a variable given the solution name, the variable name, and the scenario. If no scenario is provided, the first scenarios in the list is taken.
    """
    return solution_repository.get_unit(solution_name, variable_name)


@router.get("/get_energy_balance/{solution_name}/{node_name}/{carrier_name}")
async def get_energy_balance(
    solution_name: str,
    node_name: str,
    carrier_name: str,
    scenario: Optional[str] = None,
    year: Optional[int] = 0,
    rolling_average_size: int = 1,
) -> dict[str, list[dict[str, Any]]]:
    """
    Get the energy balance of a specific node and carrier given the solution name, the node name, the carrier, the scenario, and the year.
    If no scenario and/or year is provided, the first one is taken.
    """
    return solution_repository.get_energy_balance(
        solution_name, node_name, carrier_name, scenario, year, rolling_average_size
    )
