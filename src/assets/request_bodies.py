from pydantic import BaseModel

from src.assets.schemas import Key, Service


class PostAuthBody(BaseModel):
    apikey: Key


class PostKeysBody(BaseModel):
    service: Service
