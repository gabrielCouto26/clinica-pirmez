import boto3
from src.adapters.exceptions import FetchDataError


class DynamoDB:
    def __init__(self) -> None:
        self.client = boto3.client('dynamodb')

    def fetch(self, table: str, *args) -> list[dict]:
        """
            Retorna toda a tabela.
            Filtros ainda não implementados.
        """
        try:
            response = self.client.scan(TableName=table)
            print('response', response)
            if 'Items' not in response:
                return []

            return response['Items']

        except Exception as e:
            raise FetchDataError(e, table)
