import json
import os
from pathlib import Path
from pydantic import BaseModel, Field
from typing import Any

from ..errors import InvalidSolutionFolderError
from ..config import config

class SolutionList(BaseModel):
    """
    SolutionList defines the model of the data that is included in the solutions list endpoint.
    """

    folder_name: str
    name: str
    nodes: list[str] = Field(default=[])
    total_hours_per_year: int
    optimized_years: int
    technologies: list[str] = Field(default=[])
    carriers: list[str] = Field(default=[])
    scenarios: list[str] = Field(default=[])

    @staticmethod
    def from_path(path: str) -> "SolutionList":
        """
        Generator method to instantiate a SolutionList ins given the path of a solution.

        :param path: Path to the results folder.
        """
        # If the subfolder "energy_system" exists, we are in a model folder
        if os.path.exists(os.path.join(path, "energy_system")):
            raise InvalidSolutionFolderError()

        # Parse scenarios.json
        with open(os.path.join(path, "scenarios.json"), "r") as f:
            scenarios_json: dict[str, Any] = json.load(f)

        # List all scenarios that have a corresponding folder
        scenarios = [
            key
            for key in scenarios_json.keys()
            if os.path.isdir(os.path.join(path, f"scenario_{key}"))
        ]

        # Find first scenario folder
        # TODO This must be more flexible for different scenario types, e.g. when subscenarios exist
        if len(scenarios) == 0:
            scenario_name = ""
        elif scenarios_json[scenarios[0]]["sub_folder"] == "":
            scenario_name = f"scenario_{scenarios[0]}"
        else:
            scenario_name = f"scenario_{scenarios[0]}/scenario_{scenarios_json[scenarios[0]]['sub_folder']}"

        # Parse system.json
        with open(os.path.join(path, scenario_name, "system.json")) as f:
            system: dict[str, Any] = json.load(f)

        # Get relative path to solution folder
        relative_folder = path.replace(config.SOLUTION_FOLDER, "")
        if relative_folder[0] == "/":
            relative_folder = relative_folder[1:]
        system["folder_name"] = relative_folder

        # TODO this can change with the scenarios - it should be scenario dependent
        system["carriers"] = system["set_carriers"]
        system["technologies"] = system["set_technologies"]
        system["scenarios"] = scenarios
        system["nodes"] = system["set_nodes"]

        scenario_path = Path(path).relative_to(config.SOLUTION_FOLDER)
        system["name"] = ".".join(scenario_path.parts)
        solution = SolutionList(**system)

        return solution
