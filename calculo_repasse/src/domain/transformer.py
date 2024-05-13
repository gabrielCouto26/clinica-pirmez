import pandas as pd
from src.libs.helpers import timestamp


class Transformer:
    def __init__(self) -> None:
        pass

    @timestamp
    def calculate_share(self, data: pd.DataFrame, procedure_share: dict) -> pd.DataFrame:
        assert not data.empty, 'Invalid data provided: empty'
        assert isinstance(data, pd.DataFrame)

        try:
            data['repasse'] = pd.Series()
            data['repasse'] = (
                data['procedimento'].map(procedure_share)
                * data['valor'])
        except Exception as e:
            raise Exception(
                'Error defining "repasse" column. Original error:', e)

        try:
            final = data.groupby(['medico']).agg(
                {'repasse': 'sum'}
            ).reset_index()
        except Exception as e:
            raise Exception('Error summing "repasse". Original error:', e)

        return final
