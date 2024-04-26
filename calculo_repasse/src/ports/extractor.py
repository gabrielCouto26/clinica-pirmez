from pandas import DataFrame
from typing import Protocol


class Extractor(Protocol):
    def extract(self) -> DataFrame:
        pass


class FileExtractor:
    def __init__(self) -> None:
        self.extractor = None

    def inject_extractor(self, extractor: Extractor) -> None:
        assert extractor, 'Invalid extractor provided'
        self.extractor = extractor

    def extract(self) -> DataFrame:
        return self.extractor.extract()
