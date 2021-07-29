from fastapi import Depends, status

from src.assets.responses import Error
from src.exception import APIKeysException
from src.assets.schemas import Key, Service
from src.repository import APIKeysRepository


class AuthService:
    def __init__(self, api_keys_repository: APIKeysRepository = Depends()):
        self.repository: APIKeysRepository = api_keys_repository

    async def authenticate(self, validate_key: Key, service: Service) -> None:
        keys = await self.repository.get_apikeys(service)
        if validate_key not in keys:
            raise APIKeysException(Error(
                status=status.HTTP_403_FORBIDDEN,
                name='Forbbidden.'
            ))
        return
