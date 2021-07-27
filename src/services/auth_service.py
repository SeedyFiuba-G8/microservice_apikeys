from fastapi import Depends, status

from src.assets.responses import Error
from src.exception import APIKeysException
from src.assets.schemas import Key
from src.repository import KeysDatabase


class AuthService:
    def __init__(self, db_client: KeysDatabase = Depends()):
        self.db_client: KeysDatabase = db_client

    async def authenticate(self, validate_key: Key, api_key: Key) -> None:
        service = await self.db_client.get_service(api_key)
        keys = await self.db_client.get_auth_keys(service)
        if validate_key not in keys:
            raise APIKeysException(Error(status=status.HTTP_403_FORBIDDEN, name='Forbbidden.'))
        return
