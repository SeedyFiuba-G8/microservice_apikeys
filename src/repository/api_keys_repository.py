from typing import Dict, Set, Union
from fastapi import Depends
from pymongo import MongoClient

from src.config import config
from src.assets.schemas import Key, Service
from src.repository.client import get_db_client


class APIKeysRepository:
    def __init__(self, db_client: MongoClient = Depends(get_db_client)):
        self.db_client = db_client
        self.db_name = config.DB_DATABASE
        self.col = self.db_client[self.db_name].keys

    async def status(self) -> bool:
        _ = self.db_client.server_info()
        # print('Database info: ', info)
        return True

    async def get_owned(self, service: Service) -> Dict[Service, Key]:
        cursor = self.col.find({
            'owner': service,
            'service': {'$ne': service}
        }, {'_id': 0, 'service': 1, 'apikey': 1})
        if cursor is None:
            return None
        return {i['service']: i['apikey'] for i in cursor}

    async def get_apikeys(self, service: Service) -> Set[Key]:
        cursor = self.col.find(
            {
                'service': service,
                'owner': {'$ne': service}
            },
            {'_id': 0, 'apikey': 1}
        )
        if cursor is None:
            return None
        return {i['apikey'] for i in cursor}

    async def get_service(self, key: Key) -> Union[Service, None]:
        cursor = self.col.find_one(
            {'apikey': key},
            {'_id': 0, 'service': 1}
        )
        if cursor is None:
            return None
        return cursor['service']
