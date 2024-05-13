from typing import Protocol
from pandas import DataFrame


class FileStorage(Protocol):
    def extract(self, path: str, *args) -> DataFrame:
        pass

    def load(self, file_path: str, dest: str, *args) -> None:
        pass


class DataStorage(Protocol):
    def fetch(self, table: str, *args) -> list[dict]:
        pass

    def save(self, *args) -> None:
        pass
