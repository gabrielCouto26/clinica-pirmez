import os
from src.adapters.extractors import LocalExtractor
from src.adapters.loaders import LocalLoader
from src.ports.extractor import FileExtractor
from src.ports.loader import FileLoader
from src.domain.transformer import Transformer
from src.libs.helpers import timestamp


@timestamp
def lambda_handler(event, context):
    # FILE_PATH = os.getenv('FILE_PATH')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    FILE_PATH = f"{bucket}/{key}"
    print('\n###### -> FILE_PATH\n', FILE_PATH)

    assert FILE_PATH, 'Invalid FILE_PATH provided'

    LOAD_PATH = os.getenv('LOAD_PATH')
    assert LOAD_PATH, 'Invalid LOAD_PATH provided'

    extractor = LocalExtractor()
    loader = LocalLoader()

    file_extractor = FileExtractor()
    file_loader = FileLoader()
    transformer = Transformer()

    file_extractor.inject_extractor(extractor)
    file_loader.inject_loader(loader)

    file_data = file_extractor.extract(FILE_PATH)
    df = transformer.calculate_share(file_data)
    file_loader.load(df, LOAD_PATH)
