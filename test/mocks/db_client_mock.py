from dataclasses import dataclass

from mocks.headers import VALIDATION_KEY, API_KEY


def get_db_client_mock():
    return MongoClientMock()


class DefaultKeysColMock:
    def __init__(self):
        self.services = {VALIDATION_KEY: 'test-service'}
        pass

    def find_one(self, filters, fields):
        assert 'apikey' in filters
        assert 'service' in fields
        if filters['apikey'] not in self.services:
            return None
        return {'service': self.services[filters['apikey']]}


class KeysColMock:
    def __init__(self):
        self.keys = {'test-service': API_KEY}
        self.services = {API_KEY: 'test-service'}

    def find_one(self, filters, fields):
        assert 'apikey' in filters
        assert 'service' in fields
        if filters['apikey'] not in self.services:
            return None
        return {'service': self.services[filters['apikey']]}

    def find(self, filters, fields):
        assert 'apikey' in fields
        assert ('owner' in filters) and ('service' in filters)
        if '$ne' in filters['owner']:
            if filters['service'] not in self.keys:
                return None
            return [{'apikey': self.keys[filters['service']]}]
        elif '$ne' in filters['service']:
            if filters['owner'] not in self.keys:
                return None
            return [{'apikey': self.keys[filters['owner']], 'service': 'core'}]
        assert False, 'Error in KeyColMock.find'


@dataclass
class CollectionsMock:
    defaultkeys = DefaultKeysColMock()
    keys = KeysColMock()


class MongoClientMock:
    def __init__(self):
        self.cols = {'dev': CollectionsMock()}

    def __getitem__(self, db_name):
        if db_name != 'dev':
            raise ValueError('db name during testing should be "dev"')
        return self.cols['dev']

    def server_info(self):
        return 'Some server info'
