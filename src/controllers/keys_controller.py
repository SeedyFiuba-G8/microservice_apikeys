import random
from fastapi import Depends

from src.repository import APIKeysRepository
from src.assets.responses import GetAllKeys, GetKeys, PostKeys
from src.assets.schemas import Service


class KeysController:
    def __init__(self, repository: APIKeysRepository = Depends()):
        self.repository = repository

    async def get_all(self) -> GetAllKeys:
        all_keys = await self.repository.get_all()
        return GetAllKeys(**all_keys)

    async def get_keys(self, service: Service) -> GetKeys:
        keys = await self.repository.get_owned(service)
        return GetKeys(**keys)

    async def create_apikey(self, service: Service) -> PostKeys:
        return PostKeys(
            service=service,
            key=random.randint(0, 10)
        )
