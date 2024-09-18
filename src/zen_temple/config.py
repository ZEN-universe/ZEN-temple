import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self) -> None:
        self.SOLUTION_FOLDER: str = os.getenv("SOLUTION_FOLDER")  # type: ignore

        if self.SOLUTION_FOLDER is None:
            self.SOLUTION_FOLDER = "../outputs"

        self.check()

    def check(self) -> None:
        for key, val in self.__dict__.items():
            if val is None:
                raise Exception(f"Env-Variable {key} is missing!")


config = Config()
