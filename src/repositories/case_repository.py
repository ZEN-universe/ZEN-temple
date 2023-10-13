from ..config import config
import os


class CaseRepository:
    def get_list(self) -> list[str]:
        return os.listdir(config.CASE_FOLDER)


case_repository = CaseRepository()
