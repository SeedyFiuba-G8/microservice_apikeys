from fastapi import Depends, Response, status

from src.services import AuthService
from src.repository import APIKeysRepository
from src.assets.responses import GetKeys
from src.assets.schemas import Key, Service


class KeysController:
    def __init__(self, repository: APIKeysRepository = Depends(),
                 auth_service: AuthService = Depends()):
        self.repository = repository
        self.auth_service = auth_service

    async def get_keys(self, service: Service) -> GetKeys:
        keys = await self.repository.get_owned(service)
        return GetKeys(**keys)

    async def post_auth(self, apikey: Key, service: Service) -> Response:
        await self.auth_service.authenticate(apikey, service)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
