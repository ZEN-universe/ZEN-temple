from typing import Optional

from fastapi import APIRouter

from ..models.solution import DataResult, SolutionDetail, SolutionList
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
    ans = solution_repository.get_detail(solution_name)
    return ans


@router.get("/get_total/{solution_name}/{variable_name}")
async def get_total(
    solution_name: str, variable_name: str, scenario: Optional[str] = None
) -> DataResult:
    """
    Get the total of a variable given the solution name, the variable name, and the scenario. If no scenario is provided, the first scenarios in the list is taken.
    """
    ans = solution_repository.get_total(solution_name, variable_name, scenario)
    return ans


@router.get("/get_full_ts/{solution_name}/{variable_name}")
async def get_full_ts(
    solution_name: str,
    variable_name: str,
    scenario: Optional[str] = None,
    year: Optional[int] = None,
) -> DataResult:
    """
    Get the total of a variable given the solution name, the variable name, and the scenario. If no scenario is provided, the first scenarios in the list is taken.
    """
    ans = solution_repository.get_full_ts(solution_name, variable_name, scenario, year)
    return ans


@router.get("/get_unit/{solution_name}/{variable_name}")
async def get_unit(solution_name: str, variable_name: str) -> Optional[str]:
    """
    Get the unit of a variable given the solution name, the variable name, and the scenario. If no scenario is provided, the first scenarios in the list is taken.
    """
    ans = solution_repository.get_unit(solution_name, variable_name)
    return ans


@router.get("/get_energy_balance/{solution_name}/{node_name}/{carrier_name}")
async def get_energy_balance(
    solution_name: str,
    node_name: str,
    carrier_name: str,
    scenario: Optional[str] = None,
    year: Optional[int] = 0,
) -> dict[str, str]:
    """
    Get the energy balance of a specific node and carrier given the solution name, the node name, the carrier, the scenario, and the year.
    If no scenario and/or year is provided, the first one is taken.
    """
    ans = solution_repository.get_energy_balance(
        solution_name, node_name, carrier_name, scenario, year
    )
    return ans
