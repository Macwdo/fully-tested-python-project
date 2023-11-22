import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app=app)


@pytest.mark.parametrize(
    'url,status_code', [('record/', 404), ('records/', 200)]
)
def test_get_record_right_url(url: str, status_code: int):
    request = client.get(url)

    assert request.status_code == status_code

