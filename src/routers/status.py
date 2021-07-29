from fastapi import APIRouter, Depends, Security

from src.authorization import api_key_auth
from src.assets.responses import Health, Ping, Info
from src.controllers import StatusController

router = APIRouter(
    tags=['status'],
    dependencies=[Security(api_key_auth)]
)


@router.get('/info', response_model=Info)
async def get_info(status_controller: StatusController = Depends()):
    '''
    Get microservice info.
    '''
    return await status_controller.info()


@router.get('/health', response_model=Health)
async def get_health(status_controller: StatusController = Depends()):
    '''
    Microservice general health state reported.
    '''
    return await status_controller.health()


@router.get('/ping', response_model=Ping)
async def get_ping(status_controller: StatusController = Depends()):
    return await status_controller.ping()
