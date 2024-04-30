from pandas import DataFrame
from typing import Protocol


class Loader(Protocol):
    def load(self) -> None:
        pass


class FileLoader:
    def __init__(self) -> None:
        self.loader = None

    def inject_loader(self, loader: Loader) -> None:
        assert loader, 'Invalid loader provided'
        self.loader = loader

    def load(self, data: DataFrame, dest: str) -> None:
        try:
            self.loader.load(data, dest)
        except Exception as e:
            raise Exception('Error loading data. Original error:', e)
