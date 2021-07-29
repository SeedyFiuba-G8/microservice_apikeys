from fastapi import APIRouter, Depends, status, Security

from src.authorization import api_key_validation_auth
from src.assets.request_bodies import PostKeysBody
from src.assets.responses import PostKeys
from src.assets.schemas import Service
from src.controllers import KeysController

router = APIRouter(
    prefix='/keys',
    tags=['keys']
)


@router.get("")
async def get_keys(keys_controller: KeysController = Depends(),
                   service: Service = Security(api_key_validation_auth)):
    return await keys_controller.get_keys(service)


@router.post("/{service}", response_model=PostKeys, status_code=status.HTTP_201_CREATED)
async def post_keys(post_keys: PostKeysBody,
                    keys_controller: KeysController = Depends(),
                    _: Service = Security(api_key_validation_auth)):
    '''
    Currently mocking key creation.
    '''
    return await keys_controller.create_apikey(post_keys.service_name)
