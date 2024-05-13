import pandas as pd
from src.adapters.exceptions import FileExtractError, FileUploadError


class S3Adapter:
    def __init__(self) -> None:
        self.s3_prefix = 's3://'

    def extract(self, bucket: str, key: str) -> pd.DataFrame:
        assert bucket, 'Invalid BUCKET provided'
        assert key, 'Invalid KEY provided'
        path = f'{self.s3_prefix}{bucket}/{key}'

        try:
            return pd.read_csv(path)
        except Exception as e:
            raise FileExtractError(e, path)

    def load(self, data: pd.DataFrame, dest: str) -> None:
        if self.s3_prefix not in dest:
            dest = self.s3_prefix + dest

        try:
            assert not data.empty, 'Invalid data provided: empty'
            assert isinstance(data, pd.DataFrame)
            assert isinstance(dest, str)

            file_name = 'repasses.csv'
            dest += file_name

            data.to_csv(dest, index=False)
        except Exception as e:
            raise FileUploadError(e, dest)
