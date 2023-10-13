from sqlmodel import Field, SQLModel, Column, String
from sqlalchemy.dialects import postgresql
from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4


class Solution(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    folder_name: str
    name: str
    nodes: list[str] = Field(default=[], sa_column=Column(postgresql.ARRAY(String())))
    techologies: list[str] = Field(
        default=[], sa_column=Column(postgresql.ARRAY(String()))
    )
    carriers: list[str] = Field(
        default=[], sa_column=Column(postgresql.ARRAY(String()))
    )


class SolutionDataframe(BaseModel):
    component: str
    yearly: bool = False
    node_edit: Optional[bool] = None
    sum_techs: bool = False
    tech_type: Optional[str] = None
    reference_carrier: Optional[str] = None
    scenario: Optional[str] = None
