from sqlmodel import Field, Column, String
from sqlalchemy.dialects import postgresql
from pydantic import BaseModel
from typing import Optional
from enum import Enum
from ..config import config
import os
import json
from typing import Any
from zen_garden.model.default_config import System  # type: ignore
from zen_garden.postprocess.results import Results  # type: ignore
from pathlib import Path


class SeriesBehaviour(Enum):
    sum = "sum"
    series = "series"


class ScenarioDetail(BaseModel):
    system: System
    reference_carrier: dict[str, str]
    carriers_import: list[str]
    carriers_export: list[str]
    carriers_input: dict[str, list[str]]
    carriers_output: dict[str, list[str]]
    carriers_demand: list[str]
    edges: dict[str, str]


class SolutionDetail(BaseModel):
    name: str
    folder_name: str
    scenarios: dict[str, ScenarioDetail]
    version: str

    @staticmethod
    def from_name(name: str) -> "SolutionDetail":
        path = os.path.join(config.SOLUTION_FOLDER, *name.split("."))
        relative_path = os.path.join(*name.split("."))
        results = Results(path)
        reference_carriers = results.get_df("set_reference_carriers")

        scenario_details = {}

        for scenario_name, scenario in results.solution_loader.scenarios.items():
            system = scenario.system
            reference_carrier = reference_carriers[scenario_name].to_dict()
            df_import = results.get_df("availability_import")[scenario_name]
            df_export = results.get_df("availability_export")[scenario_name]
            df_demand = results.get_df("demand")[scenario_name]
            df_input_carriers = results.get_df("set_input_carriers")[scenario_name]
            df_output_carriers = results.get_df("set_output_carriers")[scenario_name]
            edges = results.get_df("set_nodes_on_edges")[scenario_name]
            edges_dict = edges.to_dict()
            carriers_input_dict = {
                key: val.split(",") for key, val in df_input_carriers.to_dict().items()
            }
            carriers_output_dict = {
                key: val.split(",") for key, val in df_output_carriers.to_dict().items()
            }

            for key in carriers_output_dict:
                if carriers_output_dict[key] == [""]:
                    carriers_output_dict[key] = []

            for key in carriers_input_dict:
                if carriers_input_dict[key] == [""]:
                    carriers_input_dict[key] = []

            carriers_import = list(
                df_import.loc[df_import != 0].index.get_level_values("carrier").unique()
            )
            carriers_export = list(
                df_export.loc[df_export != 0].index.get_level_values("carrier").unique()
            )

            carriers_demand = list(
                df_demand.loc[df_demand != 0].index.get_level_values("carrier").unique()
            )

            scenario_details[scenario_name] = ScenarioDetail(
                system=system,
                reference_carrier=reference_carrier,
                carriers_import=carriers_import,
                carriers_export=carriers_export,
                carriers_input=carriers_input_dict,
                carriers_output=carriers_output_dict,
                carriers_demand=carriers_demand,
                edges=edges_dict,
            )
        version = results.get_analysis().zen_garden_version
        if version is None:
            version = "0.0.0"
        return SolutionDetail(
            name=name,
            folder_name=str(relative_path),
            scenarios=scenario_details,
            version=version
        )


class Scenario(BaseModel):
    name: str
    sub_folder: str


class Solution(BaseModel):
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
    def from_path(path: str) -> "Solution":
        with open(os.path.join(path, "scenarios.json"), "r") as f:
            scenarios_json: dict = json.load(f)

        scenarios = list(scenarios_json.keys())

        scenario_path = ""

        if len(scenarios_json) > 1:
            first_scenario_name = scenarios[0]
            scenario_path = (
                "scenario_" + scenarios_json[first_scenario_name]["sub_folder"]
            )

        with open(os.path.join(path, scenario_path, "system.json")) as f:
            system: dict[str, Any] = json.load(f)

        relative_folder = path.replace(config.SOLUTION_FOLDER, "")
        if relative_folder[0] == "/":
            relative_folder = relative_folder[1:]

        system["carriers"] = system["set_carriers"]
        system["technologies"] = system["set_technologies"]
        system["folder_name"] = relative_folder
        system["scenarios"] = scenarios
        system["nodes"] = system["set_nodes"]
        scenario_path = Path(path).relative_to(config.SOLUTION_FOLDER)
        system["name"] = ".".join(scenario_path.parts)
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


class DataResult(BaseModel):
    data_csv: str
    unit: Optional[str]


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
