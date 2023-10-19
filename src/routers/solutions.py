from fastapi import APIRouter
from ..repositories.solution_repository import solution_repository
from ..models.solution import Solution
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends
from ..dependencies.database import get_session
from ..models.solution import ResultsRequest, CompleteDataRequest


router = APIRouter(prefix="/solutions", tags=["Solutions"])


@router.get("/list")
async def get_list(
    db_session: Annotated[Session, Depends(get_session)],
) -> list[Solution]:
    return solution_repository.get_list(db_session)


@router.post("/get_data")
async def get_data(request: CompleteDataRequest) -> str:
    ans = solution_repository.get_data(request)
    return ans


@router.post("/{solution_name}/df")
async def get_dataframe(solution_name: str, df_request: ResultsRequest) -> str:
    ans = solution_repository.get_dataframe_new(solution_name, df_request)
    return ans
