import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.database.base import Base
from src.database.utils import get_session
from src.main import app
from src.models.record import Record
from src.schemas.records import RecordRequest


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)


@pytest.fixture
def client(session: Session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def record_request_fixture() -> RecordRequest:
    return RecordRequest(
        content='test',
        sender_id=1,
        sender_email='sender_email@email.co',
        receiver_email='receiver_email@email.co',
        success=True,
    )


@pytest.fixture
def record_fixture(session: Session) -> Record:
    record = Record(
        content='test',
        sender_id=1,
        sender_email='sender_email@email.com',
        receiver_email='receiver_email@email.com',
        success=True,
    )
    session.add(record)
    session.commit()
    session.refresh(record)
    return record


@pytest.fixture
def records_fixture(session: Session, size: int = 100) -> list[Record]:
    records = [
        Record(
            content=f'test{i}',
            sender_id=i,
            sender_email=f'sender_email{i}@email.com',
            receiver_email=f'receiver_email{i}@email.com',
            success=True,
        )
        for i in range(size)
    ]

    session.add_all(records)
    session.commit()
    [session.refresh(record) for record in records]
    return records
