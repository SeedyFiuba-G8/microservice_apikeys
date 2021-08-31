from enum import Enum
from typing import NewType


class Service(str, Enum):
    '''
    Elegible services.
    '''
    apikeys = 'apikeys'
    core = 'core'
    gateway = 'gateway'
    users = 'users'
    sc = 'sc'
    test_service = 'test-service'


Key = NewType('Key', str)
