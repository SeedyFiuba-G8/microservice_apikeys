from fastapi import Security, Depends
from fastapi.security.api_key import APIKeyHeader

from src.assets.schemas import Key
from src.repository import KeysDatabase

api_key_header = APIKeyHeader(name='apikeys-validation-key', scheme_name='APIKeyHeader')


class UnauthorizedException(Exception):
    pass


async def api_keys_auth(api_key: Key = Security(api_key_header),
                        keys_database: KeysDatabase = Depends()) -> Key:

    service = await keys_database.get_service(api_key)

    if service is None:
        raise UnauthorizedException()
    return api_key
