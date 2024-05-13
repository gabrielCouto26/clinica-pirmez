from pandas import DataFrame
from src.ports import FileStorage


class Storage:
    def __init__(self, storage: FileStorage) -> None:
        self.storage = storage

    def extract(self, bucket: str, key: str) -> DataFrame:
        return self.storage.extract(bucket, key)

    def load(self, file_path: str, dest: str, *args) -> None:
        self.storage.load(file_path, dest, *args)
