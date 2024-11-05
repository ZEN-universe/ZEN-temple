from fastapi import APIRouter
from ..repositories.solution_repository import solution_repository
from ..models.solution import Solution, SolutionDetail, DataResult
from fastapi import UploadFile, status
from typing import Optional


router = APIRouter(prefix="/solutions", tags=["Solutions"])


@router.get("/list")
async def get_list() -> list[Solution]:
    return solution_repository.get_list()


@router.get("/get_detail/{solution_name}")
async def get_detail(solution_name: str) -> SolutionDetail:
    ans = solution_repository.get_detail(solution_name)
    return ans

@router.get("/get_total/{solution_name}/{component_name}")
async def get_total(
    solution_name: str, component_name: str, scenario: Optional[str] = None
) -> DataResult:
    ans = solution_repository.get_total(solution_name, component_name, scenario)
    return ans


@router.get("/get_unit/{solution_name}/{component_name}")
async def get_total(
    solution_name: str, component_name: str, scenario: Optional[str] = None
) -> Optional[str]:
    ans = solution_repository.get_unit(solution_name, component_name, scenario)
    return ans


@router.get("/get_energy_balance/{solution_name}/{node_name}/{carrier_name}")
async def get_energy_balance(
    solution_name: str,
    node_name: str,
    carrier_name: str,
    scenario: Optional[str] = None,
    year: Optional[int] = 0,
) -> dict[str, str]:
    ans = solution_repository.get_energy_balance(
        solution_name, node_name, carrier_name, scenario, year
    )
    return ans


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload(in_file: UploadFile) -> str:
    """
    Creates a dataset with files
    :param in_file: zip file containing the files to be uploaded
    :param title: title of the dataset
    """
    ans = await solution_repository.upload_file(in_file)

    return ans
