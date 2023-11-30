import pytest
from fastapi.testclient import TestClient


@pytest.mark.functional
def test_get_records_should_return_created_records(client: TestClient):
    
    request = client.get("records/")
    assert request.status_code == 201


@pytest.mark.unit
def test_something():
    assert 1 == 1
