import boto3
from boto3.dynamodb.types import TypeDeserializer
from decimal import Decimal
from src.adapters.exceptions import (
    FetchDataError,
    SanitizeDataError,
    DeserializeDataError)


class DynamoDB:
    def __init__(self) -> None:
        self.client = boto3.client('dynamodb')
        self.deserializer = TypeDeserializer()

    def fetch(self, table: str, *args) -> list[dict]:
        """
            Retorna toda a tabela.
            Filtros ainda não implementados.
        """
        items = self.__get_items(table)
        return self.__sanitize(items, table)

    def __get_items(self, table: str) -> list[dict]:
        try:
            response = self.client.scan(TableName=table)

            return response.get('Items', [])

        except Exception as e:
            raise FetchDataError(e, table)

    def __sanitize(self, data: list[dict], table: str) -> list[dict]:
        try:
            sanitized = []
            for obj in data:
                sanitized.append({
                    k: self.__deserialize(v)
                    for k, v in obj.items()
                })

            return sanitized
        except Exception as e:
            raise SanitizeDataError(e, table)

    def __deserialize(self, value):
        try:
            if not isinstance(value, Decimal):
                return self.deserializer.deserialize(value)

            if value % 1 == 0:
                return int(value)
            else:
                return float(value)
        except Exception as e:
            raise DeserializeDataError(e, value)
