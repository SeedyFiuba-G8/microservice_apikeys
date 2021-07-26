from typing import Dict, Optional
from pydantic import BaseModel

from src.assets.schemas import Key, Service


class GetAllKeys(BaseModel):
    defaultkeys: Dict[Service, Key]
    keys: Dict[str, Dict[Service, Key]]


class GetKeys(BaseModel):
    core: Optional[str] = None
    sc: Optional[str] = None
    users: Optional[str] = None


class PostKeys(BaseModel):
    service: Service
    key: Key


class Ping(BaseModel):
    status: str = 'ok'


class Health(BaseModel):
    database: str
