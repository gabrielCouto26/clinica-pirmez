import os
from src.adapters.extractors import LocalExtractor
from src.adapters.loaders import LocalLoader
from src.ports.extractor import FileExtractor
from src.ports.loader import FileLoader
from src.domain.transformer import Transformer
from src.libs.helpers import timestamp

print('Loading function 2')


@timestamp
def lambda_handler(event, context):
    s3_event = event['Records'][0]['s3']
    bucket = s3_event['bucket']['name']
    key = s3_event['object']['key']

    FILE_PATH = f"s3://{bucket}/{key}"
    assert FILE_PATH, 'Invalid FILE_PATH provided'

    LOAD_FOLDER = os.getenv('LOAD_FOLDER')
    assert LOAD_FOLDER, 'Invalid LOAD_FOLDER provided'

    extractor = LocalExtractor()
    loader = LocalLoader()

    file_extractor = FileExtractor()
    file_loader = FileLoader()
    transformer = Transformer()

    file_extractor.inject_extractor(extractor)
    file_loader.inject_loader(loader)

    file_data = file_extractor.extract(FILE_PATH)
    df = transformer.calculate_share(file_data)
    file_loader.load(df, LOAD_FOLDER)
