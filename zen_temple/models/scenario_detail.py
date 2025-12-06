from pydantic import BaseModel
from zen_garden.default_config import System  # type: ignore

class ScenarioDetail(BaseModel):
    """
    ScenarioDetail is the model that includes all the detail information of a scenario. It also contains the System-information from ZEN Garden.
    """

    system: System
    reference_carrier: dict[str, str]
    carriers_input: dict[str, list[str]]
    carriers_output: dict[str, list[str]]
    edges: dict[str, str]