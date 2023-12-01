import pytest
from fastapi.testclient import TestClient

from src.models.record import Record
from src.schemas.records import (
    RecordListResponse,
    RecordRequest,
    RecordResponse,
)


def test_create_record(
    record_request_fixture: RecordRequest, client: TestClient
):
    request = client.post('records/', json=record_request_fixture.model_dump())
    record = RecordResponse(**request.json())

    assert request.status_code == 201
    assert record.content == record_request_fixture.content
    assert record.id == 1


@pytest.mark.parametrize('id,status_code', ((1, 200), (2, 404)))
def test_get_record_status_code(
    record_fixture: Record, client: TestClient, id: int, status_code: int
):
    request = client.get(f'records/{id}')

    assert request.status_code == status_code


def test_get_record(record_fixture: Record, client: TestClient):
    request = client.get(f'records/{record_fixture.id}')
    record = RecordResponse(**request.json())

    assert request.status_code == 200
    assert record.id == record_fixture.id


def test_get_records(records_fixture: list[Record], client: TestClient):
    request = client.get('records/')

    records_response = RecordListResponse(**request.json())
    records = records_response.records

    assert records[0].id == records_fixture[0].id
    assert records_response.size == len(records)
    assert records_response.skip == 0
    assert records_response.limit == 100


def test_get_records_filter(records_fixture: list[Record], client: TestClient):
    request = client.get(f'records/?q={records_fixture[0].sender_email}')

    records_response = RecordListResponse(**request.json())
    records = records_response.records

    assert records[0].id == records_fixture[0].id
    assert records_response.size == len(records)


def test_get_records_pagination(
    records_fixture: list[Record], client: TestClient
):
    skip, limit = 10, 10
    request = client.get(f'records/?skip={skip}&limit={limit}')

    records_response = RecordListResponse(**request.json())
    records = records_response.records

    assert records_response.size == 10 and records_response.size == len(
        records
    )
    assert [record.id for record in records] == [
        record.id for record in records_fixture[skip : skip + limit]
    ]


@pytest.mark.parametrize('id,status_code', ((1, 204), (2, 404)))
def test_delete_record(
    record_fixture: Record,
    client: TestClient,
    id: int,
    status_code: int,
):
    request = client.delete(f'records/{id}')

    get_record_request = client.get('records/')
    records_response = RecordListResponse(**get_record_request.json())

    assert records_response.size == 0 if status_code == 204 else 1
    assert request.status_code == status_code
