from src.controllers.keys_controller import KeysController
from fastapi import APIRouter, Security, Depends, status

from src.authorization import api_key_validation_auth
from src.assets.request_bodies import PostAuthBody
from src.assets.schemas import Service

router = APIRouter(
    tags=['auth']
)


@router.post('/auth', status_code=status.HTTP_204_NO_CONTENT)
async def post_authorization(post_auth: PostAuthBody,
                             service: Service = Security(api_key_validation_auth),
                             keys_controller: KeysController = Depends()):
    return await keys_controller.post_auth(post_auth.apikey, service)
