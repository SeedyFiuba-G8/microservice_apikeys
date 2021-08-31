from pydantic import BaseModel

from src.assets.schemas import Key


class PostAuthBody(BaseModel):
    apikey: Key
