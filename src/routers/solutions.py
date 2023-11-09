from fastapi import APIRouter
from ..repositories.solution_repository import solution_repository
from ..models.solution import Solution, CompleteDataRequest
from ..models.solution import ResultsRequest
from ..utils.component_container import ComponentInfo
from fastapi import UploadFile, status
from typing import Optional


router = APIRouter(prefix="/solutions", tags=["Solutions"])


@router.get("/list")
async def get_list() -> list[Solution]:
    return solution_repository.get_list()


@router.get("/{solution_name}/components")
async def get_components(solution_name: str) -> list[ComponentInfo]:
    ans = solution_repository.get_components(solution_name)
    return ans


@router.post("/get_data")
async def get_data(request: CompleteDataRequest) -> str:
    ans = solution_repository.get_data(request)
    return ans


@router.get("/get_total/{solution_name}/{component_name}")
async def get_total(
    solution_name: str, component_name: str, scenario: Optional[str] = None
) -> str:
    ans = solution_repository.get_total(solution_name, component_name, scenario)
    return ans


@router.post("/{solution_name}/df")
async def get_dataframe(solution_name: str, df_request: ResultsRequest) -> str:
    ans = solution_repository.get_dataframe_new(solution_name, df_request)
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
