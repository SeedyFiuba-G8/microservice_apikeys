from datetime import datetime
from fastapi import Depends

from src.repository import KeysDatabase
from src.assets.responses import Health, Info, Ping


start_time = datetime.now()
creation_date = start_time.isoformat('T', 'milliseconds') + 'Z'
DESCRIPTION = 'APIKeys microservice, management of services API keys.'


class StatusController:
    def __init__(self, db: KeysDatabase = Depends()):
        self.db = db

    async def health(self) -> Health:
        database_status = 'UP' if (await self.db.status()) else 'DOWN'
        return Health(database=database_status)

    async def ping(self) -> Ping:
        return Ping(status='ok')

    async def info(self) -> Info:
        return Info(creationDate=creation_date, description=DESCRIPTION)
