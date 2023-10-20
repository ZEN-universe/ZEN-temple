import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self) -> None:
        self.SQLALCHEMY_DATABASE_URL: str = os.getenv(
            "SQLALCHEMY_DATABASE_URL"
        )  # type: ignore
        self.SOLUTION_FOLDER: str = os.getenv("SOLUTION_FOLDER")  # type: ignore
        self.CASE_FOLDER: str = os.getenv("CASE_FOLDER")  # type: ignore
        self.COMPONENTS_FOLDER_NAME: str = os.getenv("COMPONENTS_FOLDER_NAME")  # type: ignore
        self.MAXIMUM_RESULT_SIZE: int = int(os.getenv("MAXIMUM_RESULT_SIZE"))  # type: ignore

    def check(self) -> None:
        for key, val in self.__dict__.items():
            if val is None:
                raise Exception(f"Env-Variable {key} is missing!")


config = Config()
