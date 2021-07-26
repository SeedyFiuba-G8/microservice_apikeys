import random

from fastapi import Depends

from services.database_service import DatabaseService
from assets.responses import GetAllKeys, PostKey
from assets.schemas import Service


class KeysController:

    @staticmethod
    async def create_apikey(service: Service) -> PostKey:
        print('request for service: ', service)
        return PostKey(
            service=service,
            key=random.randint(0, 10)
        )

    @staticmethod
    async def get_all(db_service: DatabaseService) -> GetAllKeys:
        all_keys = await db_service.get_all_keys()
        return GetAllKeys(**all_keys)
