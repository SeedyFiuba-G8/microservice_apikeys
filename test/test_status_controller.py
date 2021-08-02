from unittest import TestCase
from fastapi.testclient import TestClient

from src.config import config
from src.main import app
from src.repository.client import get_db_client
from mocks import get_db_client_mock, api_key_header


class TestStatusController(TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app)
        app.dependency_overrides[get_db_client] = get_db_client_mock

    def test_get_ping(self):
        response = self.client.get('/ping', headers=api_key_header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok'})

    def test_get_health(self):
        response = self.client.get('/health', headers=api_key_header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'database': 'UP'})

    def test_get_info(self):
        response = self.client.get('/info', headers=api_key_header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {'creationDate': config.START_TIME,
                         'description': config.DESCRIPTION})
