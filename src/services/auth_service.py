from fastapi.exceptions import HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from fastapi import Depends

from src.assets.schemas import Key
from src.repository import KeysDatabase


class AuthService:
    def __init__(self, db_client: KeysDatabase = Depends()):
        self.db_client: KeysDatabase = db_client

    async def authenticate(self, validate_key: Key, api_key: Key) -> None:
        service = await self.db_client.get_service(api_key)
        keys = await self.db_client.get_auth_keys(service)
        if validate_key not in keys:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail='Invalid access.')
        return
