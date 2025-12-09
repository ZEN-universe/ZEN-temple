from typing import Any, Optional
from fastapi import APIRouter

from ..config import config
from ..controllers.solution_controller import (
    get_list,
    get_detail,
    get_energy_balance,
    get_full_ts,
    get_total,
    get_unit,
)
from ..models.solution_detail import SolutionDetail
from ..models.solution_list import SolutionList

router = APIRouter(prefix="/solutions", tags=["Solutions"])


@router.get("/list")
async def solution_list() -> list[SolutionList]:
    return get_list()


@router.get("/detail")
async def detail(
    solution_name: str,
) -> SolutionDetail:
    return get_detail(solution_name)


@router.get("/unit")
async def unit(solution_name: str, component: str) -> Optional[str]:
    return get_unit(solution_name, component)


@router.get("/total")
async def total(
    solution_name: str,
    components: str,
    unit_component: Optional[str] = None,
    scenario: Optional[str] = None,
    carrier: Optional[str] = None,
) -> dict[str, Optional[str]]:
    return get_total(solution_name, components, unit_component, scenario, carrier)


@router.get("/full_ts")
async def full_ts(
    solution_name: str,
    components: str,
    unit_component: Optional[str] = None,
    scenario_name: Optional[str] = None,
    year: Optional[int] = None,
    rolling_average_window_size: int = 1,
    carrier: Optional[str] = None,
) -> dict[str, Optional[list[dict[str, Any]] | str]]:
    return get_full_ts(
        solution_name,
        components,
        unit_component,
        scenario_name,
        year,
        rolling_average_window_size,
        carrier,
    )


@router.get("/energy_balance")
async def energy_balance(
    solution_name: str,
    node: str,
    carrier: str,
    scenario_name: Optional[str] = None,
    year: Optional[int] = None,
    rolling_average_window_size: int = 1,
) -> dict[str, list[dict[str, Any]]]:
    return get_energy_balance(
        solution_name, node, carrier, scenario_name, year, rolling_average_window_size
    )
