import pandas as pd


PROCEDURES_SHARE = {
    'procedimento1': 30 / 100,
    'procedimento2': 20 / 100,
    'procedimento3': 40 / 100,
}


class Transformer:
    def __init__(self) -> None:
        pass

    def calculate_share(self, data: pd.DataFrame) -> pd.DataFrame:
        assert not data.empty, 'Invalid data provided: empty'
        assert isinstance(data, pd.DataFrame)

        data['repasse'] = pd.Series()
        data['repasse'] = (
            data['procedimento'].map(PROCEDURES_SHARE)
            * data['valor'])

        final = data.groupby(['medico']).agg({'repasse': 'sum'})

        return final
