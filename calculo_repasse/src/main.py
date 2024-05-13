import os
from src.domain.transformer import Transformer
from src.domain.storage import Storage
from src.domain.database import Database
from src.domain.constants import PROCEDURE_TABLE
from src.adapters.s3_adapter import S3Adapter
from src.adapters.dynamodb import DynamoDB
from src.libs.helpers import timestamp


@timestamp
def lambda_handler(event, context):
    s3_event = event['Records'][0]['s3']
    bucket = s3_event['bucket']['name']
    key = s3_event['object']['key']

    LOAD_FOLDER = os.getenv('LOAD_FOLDER')
    assert LOAD_FOLDER, 'Invalid LOAD_FOLDER provided'

    s3_adapter = S3Adapter()
    storage = Storage(s3_adapter)

    dynamoDB = DynamoDB()
    database = Database(dynamoDB)

    transformer = Transformer()

    file_data = storage.extract(bucket, key)
    procedure_share = database.fetch(PROCEDURE_TABLE)

    df = transformer.calculate_share(file_data, procedure_share)

    storage.load(df, LOAD_FOLDER)
