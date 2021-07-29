from typing import Dict, List, Optional
from pydantic import BaseModel, validator
from datetime import datetime

from src.assets.schemas import Key, Service


class GetAllKeys(BaseModel):
    defaultkeys: Dict[Service, Key]
    keys: Dict[str, Dict[Service, Key]]


class GetKeys(BaseModel):
    core: Optional[str]
    sc: Optional[str]
    users: Optional[str]
    apikeys: Optional[str]


class PostKeys(BaseModel):
    service: Service
    key: Key


class Ping(BaseModel):
    status: str = 'ok'


class Health(BaseModel):
    database: str


class Info(BaseModel):
    creationDate: str
    description: str = 'APIKeys microservice that manages services API keys.'

    @classmethod
    @validator('creationDate')
    def datetime_check(cls, creationDate: str):
        '''
        Verify if creationDate string is formatted as datetime.
        '''
        try:
            datetime.fromisoformat(creationDate[:-1])
            return creationDate
        except ValueError:
            raise ValueError('creationDate is not formatted as datetime.')


class Error(BaseModel):
    status: int
    name: str
    message: Optional[str]
    errors: Optional[List[BaseModel]]
