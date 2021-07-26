from fastapi import APIRouter, Depends

from src.services import DatabaseService
from src.assets.responses import Health, Ping
from src.controllers import StatusController

router = APIRouter()


@router.get('/health', response_model=Health)
async def get_health(status_controller: StatusController = Depends(),
                     db_service: DatabaseService = Depends()):
    '''
    Microservice general health state reported.
    '''
    return await status_controller.get_health(db_service)


@router.get('/ping', response_model=Ping)
async def get_ping(status_controller: StatusController = Depends()):
    return await status_controller.ping()
