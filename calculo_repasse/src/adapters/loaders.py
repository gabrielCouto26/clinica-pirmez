import pandas as pd


class LocalLoader:
    def __init__(self) -> None:
        pass

    def load(self, data: pd.DataFrame, dest: str) -> None:
        assert not data.empty, 'Invalid data provided: empty'
        assert isinstance(data, pd.DataFrame)
        assert isinstance(dest, str)

        file_name = 'repasses.csv'
        dest += file_name

        data.to_csv(dest)
