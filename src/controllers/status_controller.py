
from services.database_service import DatabaseService
from assets.responses import Health, Ping


def get_db_service():
    return DatabaseService


class StatusController:

    @staticmethod
    async def get_health(db_service: DatabaseService) -> Health:
        database_status = 'UP' if (await db_service.status()) else 'DOWN'
        return Health(database=database_status)

    @staticmethod
    async def ping() -> Ping:
        return Ping(status='ok')
