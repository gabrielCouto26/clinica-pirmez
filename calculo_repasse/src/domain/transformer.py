import pandas as pd


class Transformer:
    def __init__(self) -> None:
        pass

    def calculate_share(self, data: pd.DataFrame) -> pd.DataFrame:
        assert isinstance(data, pd.DataFrame)
        return data
