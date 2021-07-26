from typing import Dict
from pydantic import BaseModel

from .schemas import Key, Service


class GetAllKeys(BaseModel):
    defaultkeys: Dict[Service, Key]
    keys: Dict[str, Dict[Service, Key]]


class PostKey(BaseModel):
    service: Service
    key: Key


class Ping(BaseModel):
    status: str = 'ok'


class Health(BaseModel):
    database: str
