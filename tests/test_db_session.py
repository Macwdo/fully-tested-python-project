import uuid
from datetime import datetime

from sqlalchemy import select

from src.models.record import Record


def test_db_fixture_session(session):
    new_record = Record(
        id=uuid.uuid4(),
        author_name='author',
        author_email='author@email.co',
        sender_email='sender@email.co',
        origin='Internal',
        success=False,
        content='content',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    session.add(new_record)
    session.commit()

    record = session.scalar(
        select(Record).where(Record.author_name == 'author')
    )
    breakpoint()

    assert record
