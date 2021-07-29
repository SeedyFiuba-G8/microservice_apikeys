from fastapi import Depends
from pymongo import MongoClient
from typing import Union

from src.config import config
from src.assets.schemas import Key, Service
from src.repository.client import get_db_client


class ValidKeysRepository:
    def __init__(self, db_client: MongoClient = Depends(get_db_client)):
        self.db_client = db_client
        self.db_name = config.DB_DATABASE
        self.col = self.db_client[self.db_name].defaultkeys

    async def status(self) -> bool:
        _ = self.db_client.server_info()
        return True

    async def get_service(self, key: Key) -> Union[Service, None]:
        cursor = self.col.find_one(
            {'apikey': key},
            {'_id': 0, 'service': 1}
        )
        if cursor is None:
            return None
        return cursor['service']
