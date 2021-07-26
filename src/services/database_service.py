from typing import Dict, Any

from repository import get_db_client


class DatabaseService:

    @staticmethod
    async def get_all_keys() -> Dict[str, Any]:
        return {'defaultkeys': {'apikeys': 1, 'core': 2, 'gateway': 3, 'users': 4, 'smartcontract': 5},
                'keys': {'servicename': {'apikeys': 12}, 'otherservice': {'core': 14}}}

    @staticmethod
    async def status() -> bool:
        info = get_db_client().server_info()
        print('Database info: ', info)
        return True
