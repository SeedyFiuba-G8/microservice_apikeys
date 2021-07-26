from fastapi import APIRouter, Depends


from services import DatabaseService
from assets.responses import PostKey
from assets.schemas import Service
from controllers import KeysController

router = APIRouter(
    prefix='/keys',
    tags=['keys']
)


@router.get("")
async def get_all_keys(keys_controller: KeysController = Depends(),
                       db_service: DatabaseService = Depends()):
    return await keys_controller.get_all(db_service)


@router.post("/{service}", response_model=PostKey)
async def post_key(service: Service,
                   keys_controller: KeysController = Depends()):
    return await keys_controller.create_apikey(service)
