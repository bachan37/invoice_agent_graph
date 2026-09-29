from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models in the application.

    Alembic reads `Base.metadata` to automatically detect table changes and generate migration scripts.
    """

    pass