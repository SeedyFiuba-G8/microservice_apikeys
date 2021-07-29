from fastapi import Security, Depends, status
from fastapi.security.api_key import APIKeyHeader

from src.assets.responses import Error
from src.exception import APIKeysException
from src.assets.schemas import Key, Service
from src.repository import APIKeysRepository, ValidKeysRepository

api_key_header = APIKeyHeader(name='x-api-key', scheme_name='APIKeyHeader')
api_key_validation = APIKeyHeader(name='apikeys-validation-key', scheme_name='APIKeyHeader')


async def api_key_auth(api_key: Key = Security(api_key_header),
                       api_keys_repository: APIKeysRepository = Depends()) -> Service:
    service = await api_keys_repository.get_service(api_key)

    if service is None:
        raise APIKeysException(Error(status=status.HTTP_403_FORBIDDEN, name='Forbbidden.'))
    return service


async def api_key_validation_auth(api_key: Key = Security(api_key_validation),
                                  valid_keys_repository: ValidKeysRepository = Depends()) -> Service:
    service = await valid_keys_repository.get_service(api_key)

    if service is None:
        raise APIKeysException(Error(status=status.HTTP_403_FORBIDDEN, name='Forbbidden.'))
    return service
