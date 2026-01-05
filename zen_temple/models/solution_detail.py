import os
from pydantic import BaseModel
from zen_garden.postprocess.results import Results  # type: ignore

from .scenario_detail import ScenarioDetail
from ..config import config
from ..versions import get_variable_name

class SolutionDetail(BaseModel):
    """
    SolutionDetail is the model that includes all the detail information of a solution. This includes the ScenarioDetail for all scenarios of a solution.
    """

    name: str
    folder_name: str
    scenarios: dict[str, ScenarioDetail]
    version: str
    objective: str

    @staticmethod
    def from_path(path: str) -> "SolutionDetail":
        """
        Generator that instantiates a SolutionDetail given the path of a solution.
        It creates a Solution-instance of ZEN Gardens solution class and extracts the necessary dataframes from this solution.

        :param path: Path to the results folder.
        """
        name = os.path.split(path)[-1]
        relative_path = os.path.relpath(path, start=config.SOLUTION_FOLDER)
        results = Results(path, enable_cache=False)
        results_version = results.get_analysis().zen_garden_version
        scenario_details = {}

        for scenario_name, scenario in results.solution_loader.scenarios.items():
            system = scenario.system
            reference_carriers = results.get_df(
                get_variable_name("set_reference_carriers", results_version),
                scenario_name=scenario_name,
            ).to_dict()

            df_input_carriers = results.get_df(
                get_variable_name("set_input_carriers", results_version),
                scenario_name=scenario_name,
            )

            df_output_carriers = results.get_df(
                get_variable_name("set_output_carriers", results_version),
                scenario_name=scenario_name,
            )

            edges = results.get_df(
                get_variable_name("set_nodes_on_edges", results_version),
                scenario_name=scenario_name,
            )

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

            scenario_details[scenario_name] = ScenarioDetail(
                system=system,
                reference_carrier=reference_carriers,
                carriers_input=carriers_input_dict,
                carriers_output=carriers_output_dict,
                edges=edges_dict,
            )

        version = results.get_analysis().zen_garden_version
        if version is None:
            version = "0.0.0"

        objective = results.get_analysis().objective
        if objective is None:
            objective = ""

        return SolutionDetail(
            name=name,
            folder_name=str(relative_path),
            scenarios=scenario_details,
            version=version,
            objective=objective,
        )
