from ..config import config
from zen_garden.postprocess.results import Results  # type: ignore
from ..models.solution import Solution, ResultsRequest, CompleteDataRequest
import os
from sqlalchemy.orm import Session
from sqlmodel import select
import pandas as pd
from time import perf_counter
import numpy.typing as npt
import numpy as np
from ..utils.numpy_utils import (
    summarize_np_array,
    IndexType,
    create_deep_csv,
    aggregate_time_steps,
)
import json
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

        ndarray_path = os.path.join(base_path, request.component + ".npy")
        index_path = os.path.join(base_path, request.component + ".json")

        with open(index_path, "r") as f:
            index: IndexType | None = json.load(f)

        if index is None:
            raise HTTPException(status_code=404, detail="Could not find data index.")

        np_array: npt.NDArray[np.float_] = np.load(ndarray_path)

        result, index = summarize_np_array(np_array, index, request.data_request)

        if request.aggregate_years:
            system_path = os.path.join(solution_folder, "system.json")
            with open(system_path, "r") as f:
                system_dict = json.load(f)

            time_steps = 1

            if "aggregated_time_steps_per_year" in system_dict:
                time_steps = system_dict["aggregated_time_steps_per_year"]

            result, index = aggregate_time_steps(np_array, time_steps, index=index)

            if index is None:
                raise HTTPException(
                    status_code=404, detail="Could not succesfully create index."
                )

        if result.size > config.MAXIMUM_RESULT_SIZE:
            raise HTTPException(
                status_code=413,
                detail="""
                Too many datapoints.
                Consider selecting a subset of indices or aggregate over years.
                """,
            )

        res = create_deep_csv(result, index)

        return res

    def get_dataframe_new(self, solution_name: str, df_request: ResultsRequest) -> str:
        request = df_request.to_data_request(solution_name)
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


solution_repository = SolutionRepository()
