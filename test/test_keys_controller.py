from unittest import TestCase
from fastapi.testclient import TestClient

from src.main import app
from src.repository.client import get_db_client
from mocks import get_db_client_mock, api_key_validation_header, API_KEY


class TestStatusController(TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app)
        app.dependency_overrides[get_db_client] = get_db_client_mock

    def test_get_keys_with_valid_key(self):
        response = self.client.get('/keys', headers=api_key_validation_header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'core': API_KEY})

    def test_keys_with_invalid_key(self):
        response = self.client.get('/keys', headers={'apikeys-validation-key': 'bla-bla'})
        self.assertEqual(response.status_code, 403)

    def test_post_auth_with_valid_apikey(self):
        response = self.client.post('/auth',
                                    headers=api_key_validation_header,
                                    json={'apikey': API_KEY})
        self.assertEqual(response.status_code, 204)

    def test_post_auth_with_wrong_apikey(self):
        response = self.client.post('/auth',
                                    headers=api_key_validation_header,
                                    json={'apikey': 'not-valid'})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json(), {'status': 403, 'name': 'Forbbidden.'})
