from src.authorization import api_keys_auth
from fastapi import APIRouter, Depends, status

from src.assets.request_bodies import PostKeysBody
from src.assets.responses import PostKeys
from src.assets.schemas import Key
from src.controllers import KeysController

router = APIRouter(
    prefix='/keys',
    tags=['keys']
)


@router.get("")
async def get_keys(keys_controller: KeysController = Depends(),
                   api_key: Key = Depends(api_keys_auth)):
    return await keys_controller.get_keys(api_key)


@router.post("/{service}", response_model=PostKeys, status_code=status.HTTP_201_CREATED)
async def post_keys(post_keys: PostKeysBody,
                    keys_controller: KeysController = Depends(),
                    _: Key = Depends(api_keys_auth)):
    '''
    Currently mocking key creation.
    '''
    return await keys_controller.create_apikey(post_keys.service_name)
