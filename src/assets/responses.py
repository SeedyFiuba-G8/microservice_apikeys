from typing import List, Optional
from pydantic import BaseModel, validator
from datetime import datetime

from src.assets.schemas import Key


class GetKeys(BaseModel):
    core: Optional[Key]
    sc: Optional[Key]
    users: Optional[Key]
    apikeys: Optional[Key]


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
