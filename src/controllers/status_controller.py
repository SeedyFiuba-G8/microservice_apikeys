from fastapi import Depends

from src.config import config
from src.repository import APIKeysRepository, ValidKeysRepository
from src.assets.responses import Health, Info, Ping


class StatusController:
    def __init__(self, api_keys_repository: APIKeysRepository = Depends(),
                 valid_keys_repository: ValidKeysRepository = Depends()):
        self.api_keys = api_keys_repository
        self.valid_keys = valid_keys_repository

    async def health(self) -> Health:
        bool_db_status = (await self.api_keys.status() and await self.valid_keys.status())
        database_status = 'UP' if bool_db_status else 'DOWN'
        return Health(database=database_status)

    async def ping(self) -> Ping:
        return Ping(status='ok')

    async def info(self) -> Info:
        return Info(creationDate=config.START_TIME, description=config.DESCRIPTION)
