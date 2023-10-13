from ..config import config
from zen_garden.postprocess.results import Results  # type: ignore
from ..models.solution import Solution, SolutionDataframe
import os
from sqlalchemy.orm import Session
from sqlmodel import select
import pandas


class SolutionRepository:
    def get_list(self, db_session: Session) -> list[Solution]:
        query = select(Solution)
        response = db_session.execute(query)
        print(response)
        datasets = response.scalars().all()
        return datasets

    def get_dataframe(self, solution_name: str, df_request: SolutionDataframe) -> str:
        path = os.path.join(config.SOLUTION_FOLDER, solution_name)
        argument_dictionary = {
            key: val for key, val in df_request.dict().items() if val is not None
        }
        res: pandas.DataFrame = Results(path).get_summary_df(**argument_dictionary)
        print(res)
        res = res.reset_index()
        years = [i for i in res.columns if isinstance(i, int)]
        others = [i for i in res.columns if not isinstance(i, int)]
        res = pandas.melt(res, id_vars=others, var_name="year", value_vars=years)
        return res.to_csv()


solution_repository = SolutionRepository()
