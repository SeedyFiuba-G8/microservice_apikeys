from fastapi import APIRouter, Depends, Security

from src.assets.responses import GetKeys
from src.authorization import api_key_validation_auth
from src.assets.schemas import Service
from src.controllers import KeysController

router = APIRouter(
    prefix='/keys',
    tags=['keys']
)


@router.get("", response_model=GetKeys, response_model_exclude_none=True)
async def get_keys(keys_controller: KeysController = Depends(),
                   service: Service = Security(api_key_validation_auth)):
    return await keys_controller.get_keys(service)
