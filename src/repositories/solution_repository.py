from ..config import config
from zen_garden.postprocess.results import Results  # type: ignore
from ..models.solution import Solution, ResultsRequest, CompleteDataRequest
import os
from sqlalchemy.orm import Session
from sqlmodel import select
import pandas as pd
from time import perf_counter
from ..utils.component_container import ComponentContainer, ComponentInfo
from fastapi import HTTPException


class SolutionRepository:
    def get_list(self, db_session: Session) -> list[Solution]:
        query = select(Solution)
        response = db_session.execute(query)
        datasets = response.scalars().all()
        return datasets

    def get_data(self, request: CompleteDataRequest) -> str:
        solution_folder = os.path.join(config.SOLUTION_FOLDER, request.solution_name)
        base_path = os.path.join(
            solution_folder,
            config.COMPONENTS_FOLDER_NAME,
            request.scenario,
        )

        try:
            component_container = ComponentContainer.load(request.component, base_path)
        except ValueError:
            raise HTTPException(404, "Scenario or Component not found.")

        summarized_container = component_container.summarize_np_array(
            request.data_request
        )

        if request.aggregate_years and not summarized_container.info.yearly:
            summarized_container = summarized_container.aggregate_time_steps()

        if summarized_container.data.size > config.MAXIMUM_RESULT_SIZE:
            raise HTTPException(
                status_code=413,
                detail="""
                Too many datapoints.
                Consider selecting a subset of indices or aggregate over years.
                """,
            )
        res = summarized_container.create_deep_csv()

        return res

    def get_dataframe_new(self, solution_name: str, df_request: ResultsRequest) -> str:
        request = df_request.to_data_request(solution_name)
        print(request)
        return self.get_data(request)

    def get_dataframe(self, solution_name: str, df_request: ResultsRequest) -> str:
        path = os.path.join(config.SOLUTION_FOLDER, solution_name)
        argument_dictionary = {
            key: val for key, val in df_request.dict().items() if val is not None
        }

        start = perf_counter()
        results = Results(path)
        print(f"Loading results took {perf_counter() - start}")

        if "scenario" in argument_dictionary:
            request_scenario = "scenario_" + argument_dictionary["scenario"]
            if request_scenario not in results.results:
                argument_dictionary["scenario"] = None
            else:
                argument_dictionary["scenario"] = request_scenario

        start = perf_counter()
        res: pd.DataFrame = results.get_summary_df(**argument_dictionary)
        res = res.reset_index()
        years = [i for i in res.columns if isinstance(i, int)]
        others = [i for i in res.columns if not isinstance(i, int)]
        print(res)
        res = pd.melt(res, id_vars=others, var_name="year", value_vars=years)

        return res.to_csv()

    def get_components(self, solution_name: str, scenario: str) -> list[ComponentInfo]:
        ans: list[ComponentInfo] = []
        solution_folder = os.path.join(
            config.SOLUTION_FOLDER,
            solution_name,
            config.COMPONENTS_FOLDER_NAME,
            scenario,
        )

        ans = [
            ComponentInfo.from_path(os.path.join(solution_folder, i))
            for i in os.listdir(solution_folder)
            if i.endswith(".json")
        ]

        return ans


solution_repository = SolutionRepository()
