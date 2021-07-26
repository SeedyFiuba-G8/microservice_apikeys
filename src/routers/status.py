from src.authorization import api_keys_auth
from fastapi import APIRouter, Depends

from src.assets.responses import Health, Ping
from src.controllers import StatusController

router = APIRouter(
    tags=['status'],
    dependencies=[Depends(api_keys_auth)]
)


@router.get('/health', response_model=Health)
async def get_health(status_controller: StatusController = Depends()):
    '''
    Microservice general health state reported.
    '''
    return await status_controller.get_health()


@router.get('/ping', response_model=Ping)
async def get_ping(status_controller: StatusController = Depends()):
    return await status_controller.ping()
