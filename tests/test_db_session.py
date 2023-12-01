from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.record import Record


def test_db_fixture_session(session: Session):
    new_record = Record(
        sender_id=1,
        sender_email='author@email.co',
        receiver_email='sender@email.co',
        success=False,
        content='content',
    )
    session.add(new_record)
    session.commit()

    record = session.scalar(select(Record).where(Record.sender_id == 1))
    assert record
