from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from src import models  # noqa: F401, E402
