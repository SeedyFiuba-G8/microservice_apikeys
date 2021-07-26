import random
from fastapi import Depends

from src.repository import KeysDatabase
from src.assets.responses import GetAllKeys, GetKeys, PostKeys
from src.assets.schemas import Key, Service


class KeysController:
    def __init__(self, db: KeysDatabase = Depends()):
        self.db = db

    async def get_all(self) -> GetAllKeys:
        all_keys = await self.db.get_all()
        return GetAllKeys(**all_keys)

    async def get_keys(self, api_key: Key) -> GetKeys:
        keys = await self.db.get_owned_keys(await self.db.get_service(api_key))
        return GetKeys(**keys)

    async def create_apikey(self, service: Service) -> PostKeys:
        return PostKeys(
            service=service,
            key=random.randint(0, 10)
        )
