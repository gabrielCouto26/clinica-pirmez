import pandas as pd
from libs.helpers import timestamp, type_check


PROCEDURES_SHARE = {
    'procedimento1': 30 / 100,
    'procedimento2': 20 / 100,
    'procedimento3': 40 / 100,
}


class Transformer:
    def __init__(self) -> None:
        pass

    @timestamp
    @type_check
    def calculate_share(self, data: pd.DataFrame) -> pd.DataFrame:
        assert not data.empty, 'Invalid data provided: empty'
        assert isinstance(data, pd.DataFrame)

        try:
            data['repasse'] = pd.Series()
            data['repasse'] = (
                data['procedimento'].map(PROCEDURES_SHARE)
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
