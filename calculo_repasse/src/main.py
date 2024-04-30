import os
from adapters.extractors import LocalExtractor
from adapters.loaders import LocalLoader
from ports.extractor import FileExtractor
from ports.loader import FileLoader
from domain.transformer import Transformer
from libs.helpers import timestamp


@timestamp
def main():
    FILE_PATH = os.getenv('FILE_PATH')
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


if __name__ == '__main__':
    main()
