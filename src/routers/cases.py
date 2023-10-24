from fastapi import APIRouter
from ..repositories.case_repository import case_repository
import zen_garden.model  # type: ignore
import os


router = APIRouter(prefix="/cases", tags=["Cases"])


@router.get("/list")
async def get_list() -> list[str]:
    return case_repository.get_list()


@router.post("/{case_name}/solve")
async def start(case_name: str, config: zen_garden.model.Config) -> list[str]:
    return os.listdir(config.SOLUTION_FOLDER)
