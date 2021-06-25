"""Models for the auth API."""
from contextlib import contextmanager

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
)
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore

from demo.config import Config

metadata = MetaData()
Base = declarative_base(metadata=metadata)

db = create_engine(Config().DATABASE_URI)
Session = sessionmaker(db)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class Users(Base):
    """Base user table that identifies all of our users and their status."""

    __tablename__ = "users"
    account = Column(String, primary_key=True)
    active = Column(Boolean, nullable=False, default=False, index=True)
    is_demo = Column(Boolean, nullable=False, default=False, index=True)

    def __repr__(self):
        return (
            f"<Users account={self.account}, active={self.active},"
            f"scopes={self.scopes}, data={self.data}>"
        )
