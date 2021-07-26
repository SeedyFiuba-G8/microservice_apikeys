from fastapi import APIRouter, Security, Depends, status, Response

from src.authorization import api_keys_auth
from src.services import AuthService
from src.assets.request_bodies import PostAuthBody
from src.assets.schemas import Key

router = APIRouter(
    tags=['auth']
)


@router.post('/auth', status_code=status.HTTP_204_NO_CONTENT)
async def post_authorization(post_auth: PostAuthBody, api_key: Key = Security(api_keys_auth),
                             auth_service: AuthService = Depends()):
    await auth_service.authenticate(post_auth.apikey, api_key)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
