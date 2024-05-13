from src.ports import DataStorage
from src.libs.helpers import timestamp


class Database:
    def __init__(self, database: DataStorage) -> None:
        self.database = database

    @timestamp
    def fetch(self, table: str) -> list[dict]:
        assert isinstance(table, str)

        response = self.database.fetch(table)
        return self.__get_shares(response)

    def __get_shares(self, data: list[dict]) -> list[dict]:
        shares = {}
        for item in data:
            name = item['name']
            share = item['share']
            shares[name] = share / 100

        return shares
