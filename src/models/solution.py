from sqlmodel import Field, SQLModel, Column, String
from sqlalchemy.dialects import postgresql
from pydantic import BaseModel
from typing import Optional
from enum import Enum
from src.config import config
import os
import json
from uuid import UUID, uuid4
from typing import Any


class SeriesBehaviour(Enum):
    sum = "sum"
    series = "series"


class Solution(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    folder_name: str
    name: str
    nodes: list[str] = Field(default=[], sa_column=Column(postgresql.ARRAY(String())))
    total_hours_per_year: int
    optimized_years: int
    technologies: list[str] = Field(
        default=[], sa_column=Column(postgresql.ARRAY(String()))
    )
    carriers: list[str] = Field(
        default=[], sa_column=Column(postgresql.ARRAY(String()))
    )
    scenarios: list[str] = Field(
        default=[], sa_column=Column(postgresql.ARRAY(String()))
    )

    @staticmethod
    def from_name(name: str) -> "Solution":
        with open(os.path.join(config.SOLUTION_FOLDER, name, "system.json")) as f:
            system: dict[str, Any] = json.load(f)

        scenarios = [
            i
            for i in os.listdir(os.path.join(config.SOLUTION_FOLDER, name))
            if i.startswith("scenario_")
        ]

        if len(scenarios) == 0:
            scenarios = ["scenario_"]

        system["carriers"] = system["set_carriers"]
        system["technologies"] = system["set_technologies"]
        system["folder_name"] = name.split("/")[-1]
        system["scenarios"] = scenarios
        system["nodes"] = system["set_nodes"]
        system["name"] = name.split("/")[-1]
        solution = Solution(**system)

        return solution


class IndexSet(BaseModel):
    index_title: str
    behaviour: SeriesBehaviour = SeriesBehaviour.series
    indices: list[str] = []


class DataRequest(BaseModel):
    default: SeriesBehaviour = SeriesBehaviour.series
    index_sets: list[IndexSet] = []


class CompleteDataRequest(BaseModel):
    solution_name: str
    component: str
    scenario: str = "scenario_"
    data_request: DataRequest
    aggregate_years: bool = False


class ResultsRequest(BaseModel):
    component: str
    yearly: bool = False
    node_edit: Optional[str] = None
    sum_techs: bool = False
    tech_type: Optional[str] = None
    reference_carrier: Optional[str] = None
    scenario: Optional[str] = None

    def to_data_request(self, solution_name: str) -> CompleteDataRequest:
        data_request = DataRequest()
        index_sets: list[IndexSet] = []

        if self.node_edit is not None and self.node_edit != "all":
            index_sets.append(
                IndexSet(
                    index_title="node",
                    behaviour=SeriesBehaviour.series,
                    indices=[self.node_edit],
                )
            )

        if (
            self.sum_techs is not None or self.tech_type
        ) is not None and self.tech_type != "all":
            tech_index = IndexSet(
                index_title="technology", behaviour=SeriesBehaviour.series
            )
            if self.sum_techs:
                tech_index.behaviour = SeriesBehaviour.sum
            if self.tech_type is not None:
                tech_index.indices = [self.tech_type]
            index_sets.append(tech_index)

        if self.reference_carrier is not None and self.reference_carrier != "all":
            index_sets.append(
                IndexSet(
                    index_title="carrier",
                    behaviour=SeriesBehaviour.series,
                    indices=[self.reference_carrier],
                )
            )

        data_request.index_sets = index_sets

        request = CompleteDataRequest(
            solution_name=solution_name,
            component=self.component,
            data_request=data_request,
            aggregate_years=self.yearly,
        )

        if self.scenario is not None:
            request.scenario = "scenario_" + self.scenario

        return request
