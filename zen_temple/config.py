import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self) -> None:
        self.SOLUTION_FOLDER: str = os.getenv("SOLUTION_FOLDER", "./outputs")
        self.EPS = float(os.getenv("EPS", 1e-6))
        self.RESPONSE_SIGNIFICANT_DIGITS = int(os.getenv("RESPONSE_SIGNIFICANT_DIGITS", 4))

        self.check()

    def check(self) -> None:
        for key, val in self.__dict__.items():
            if val is None:
                raise Exception(f"Env-Variable {key} is missing!")


config = Config()
