from fastapi import Depends

from src.repository import KeysDatabase
from src.assets.responses import Health, Ping


class StatusController:
    def __init__(self, db: KeysDatabase = Depends()):
        self.db = db

    async def get_health(self) -> Health:
        database_status = 'UP' if (await self.db.status()) else 'DOWN'
        return Health(database=database_status)

    async def ping(self) -> Ping:
        return Ping(status='ok')
