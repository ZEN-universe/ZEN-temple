from ..config import config
from zen_garden.postprocess.results import Results  # type: ignore
from ..models.solution import (
    Solution,
    ResultsRequest,
    SolutionDetail,
    DataResult,
)
import os
import pandas as pd
from time import perf_counter
from fastapi import HTTPException, UploadFile
from zipfile import ZipFile
from typing import Optional
from functools import cache
from os import walk


class SolutionRepository:
    def get_list(self) -> list[Solution]:
        solutions_folders: set[str] = set()
        ans = []
        for dirpath, dirnames, filenames in walk(config.SOLUTION_FOLDER):
            if "scenarios.json" in filenames:
                solutions_folders.add(dirpath)

        for folder in solutions_folders:
            try:
                ans.append(Solution.from_path(folder))
            except (FileNotFoundError, NotADirectoryError):
                continue
        return ans

    @cache
    def get_detail(self, solution_name: str) -> SolutionDetail:
        return SolutionDetail.from_name(solution_name)

    @cache
    def get_total(
        self, solution: str, component: str, scenario: Optional[str] = None
    ) -> DataResult:
        solution_folder = os.path.join(config.SOLUTION_FOLDER, *solution.split("."))
        results = Results(solution_folder)
        unit = self.get_unit(solution, component, scenario)
        try:
            total: pd.DataFrame | pd.Series = results.get_total(
                component, scenario_name=scenario
            )
        except KeyError:
            raise HTTPException(status_code=404, detail=f"{component} not found!")

        if type(total) is not pd.Series:
            total = total.loc[~(total == 0).all(axis=1)]

        return DataResult(data_csv=str(total.to_csv()), unit=unit)

    def get_unit(
        self, solution: str, component: str, scenario: Optional[str] = None
    ) -> Optional[str]:
        solution_folder = os.path.join(config.SOLUTION_FOLDER, *solution.split("."))
        results = Results(solution_folder)

        try:
            unit: str | pd.DataFrame = results.get_unit(component)
            if type(unit) is str:
                unit = pd.DataFrame({0: [unit]})
            unit = str(unit.to_csv())
        except Exception:
            unit = None
        return unit

    @cache
    def get_energy_balance(
        self,
        solution: str,
        node: str,
        carrier: str,
        scenario: Optional[str] = None,
        year: Optional[int] = None,
    ) -> dict[str, str]:
        solution_folder = os.path.join(config.SOLUTION_FOLDER, *solution.split("."))
        results = Results(solution_folder)

        if year is None:
            year = 0
        energy_balance: dict[str, pd.DataFrame] = results.get_energy_balance_dataframes(
            node, carrier, year, scenario
        )

        ans = {key: val.drop_duplicates() for key, val in energy_balance.items()}

        for key, series in ans.items():
            if key == "demand":
                continue

            if type(series) is not pd.Series:
                ans[key] = series.loc[~(series == 0).all(axis=1)]

        ans = {key: val.to_csv() for key, val in ans.items()}

        return ans

    def get_dataframe(self, solution_name: str, df_request: ResultsRequest) -> str:
        path = os.path.join(config.SOLUTION_FOLDER, *solution_name.split("."))
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
        res = pd.melt(res, id_vars=others, var_name="year", value_vars=years)

        return res.to_csv()

    async def upload_file(self, in_file: UploadFile) -> str:
        file_path = os.path.join("./", str(in_file.filename))

        async def upload() -> None:
            pass
            # async with aiofiles.open(file_path, "wb") as out_file:
            #    while content := await in_file.read():  # async read chunk
            #        await out_file.write(content)  # async write chunk

        await upload()

        with ZipFile(file_path, "r") as zip:
            contents: list[str] = zip.namelist()
            print(contents)

        return "Success"


solution_repository = SolutionRepository()
