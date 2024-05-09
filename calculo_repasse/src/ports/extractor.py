from pandas import DataFrame
from typing import Protocol
from src.libs.helpers import timestamp


class Extractor(Protocol):
    def extract(self) -> DataFrame:
        pass


class FileExtractor:
    def __init__(self) -> None:
        self.extractor = None

    def inject_extractor(self, extractor: Extractor) -> None:
        assert extractor, 'Invalid extractor provided'
        self.extractor = extractor

    @timestamp
    def extract(self, path: str) -> DataFrame:
        try:
            return self.extractor.extract(path)
        except Exception as e:
            raise Exception('Error extracting data. Original error:', e)
