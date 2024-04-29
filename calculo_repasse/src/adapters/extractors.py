import pandas as pd


class DropboxExtractor:
    def __init__(self) -> None:
        pass

    def extract(self) -> None:
        pass


class LocalExtractor:
    def __init__(self) -> None:
        pass

    def extract(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)
