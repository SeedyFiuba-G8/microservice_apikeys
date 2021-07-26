from typing import Dict, Any, List, Set, Tuple, Union
from fastapi import Depends
from pymongo import MongoClient
from pymongo.errors import OperationFailure

from src.config import config
from src.assets.schemas import Key, Service
from src.repository.client import get_db_client


class KeysDatabase:
    def __init__(self, db_client: MongoClient = Depends(get_db_client)):
        self.db_client: MongoClient = db_client
        self.db_name: str = config.DB_DATABASE
        self.db = self.db_client[self.db_name]

    async def status(self) -> bool:
        _ = self.db_client.server_info()
        # print('Database info: ', info)
        return True

    async def add_key(self, service: Service, key: Key, collection='keys') -> bool:
        ins_one = self.db[collection].insert_one({'service': service, 'apikey': key})
        return ins_one.acknowledged

    async def add_keys(self, services_keys: List[Tuple[Service, Key]], collection='keys') -> bool:
        ins_many = self.db[collection].insert_many(
            [{'service': service, 'apikey': key} for service, key in services_keys])
        return ins_many.acknowledged

    async def get_all(self, collection='keys') -> Dict[str, Any]:
        cursor = self.db[collection].find({})
        if cursor is None:
            return None
        return cursor

    async def get_owned_keys(self, service: Service, collection='keys') -> Dict[Service, Key]:
        cursor = self.db[collection].find({
            'owner': service,
            'service': {'$ne': service}
        }, {'_id': 0, 'service': 1, 'apikey': 1})   # TMP
        if cursor is None:
            return None
        return {i['service']: i['apikey'] for i in cursor}

    async def get_auth_keys(self, service: Service, collection='keys') -> Set[Key]:
        cursor = self.db[collection].find(
            {
                'service': service,
                'owner': {'$ne': service}
            },
            {'_id': 0, 'apikey': 1}
        )   # TMP
        if cursor is None:
            return None
        return {i['apikey'] for i in cursor}

    async def get_service(self, key: Key) -> Union[Service, None]:
        cursor = self.db['defaultkeys'].find_one(
            {'apikey': key},
            {'_id': 0, 'service': 1}
        )
        if cursor is None:
            return None
        return cursor['service']

    async def clear(self, collection='keys') -> None:
        try:
            self.db[collection].delete_many({})
        except OperationFailure:
            print(f"ERROR: user: {config.DB_USER} doesn't have write permissions on "
                  f"{config.DB_DATABASE}.{collection}")
