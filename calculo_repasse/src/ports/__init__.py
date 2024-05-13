from typing import Protocol
from pandas import DataFrame


class FileStorage(Protocol):
    def fetch(self, path: str, *args) -> DataFrame:
        pass

    def load(self, file_path: str, dest: str, *args) -> None:
        pass
