from .models.solution import Solution
from .config import config
from sqlmodel import select
from sqlmodel import Session
from .dependencies.database import engine
import os
import json


def update_solutions() -> None:
    with Session(engine) as session:
        for folder in os.listdir(config.SOLUTION_FOLDER):
            statement = select(Solution).where(Solution.name == folder)
            results = session.exec(statement)
            solution: Solution | None = results.one_or_none()

            if solution is None:
                solution = Solution()

            with open(os.path.join(config.SOLUTION_FOLDER, folder, "system.json")) as f:
                system = json.load(f)

            solution.carriers = system["set_carriers"]
            solution.techologies = system["set_technologies"]
            solution.folder_name = folder
            solution.nodes = system["set_nodes"]
            solution.name = folder

            session.add(solution)

        session.commit()