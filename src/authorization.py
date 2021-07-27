from fastapi import Security, Depends, status
from fastapi.security.api_key import APIKeyHeader

from src.assets.responses import Error
from src.exception import APIKeysException
from src.assets.schemas import Key
from src.repository import KeysDatabase

api_key_header = APIKeyHeader(name='apikeys-validation-key', scheme_name='APIKeyHeader')


async def api_keys_auth(api_key: Key = Security(api_key_header),
                        keys_database: KeysDatabase = Depends()) -> Key:
    print(api_key)
    service = await keys_database.get_service(api_key)

    if service is None:
        raise APIKeysException(Error(status=status.HTTP_403_FORBIDDEN, name='Forbbidden.'))
    return api_key
