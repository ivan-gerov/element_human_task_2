"""Models for the auth API."""
from contextlib import contextmanager

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Float,
    ForeignKey,
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
            f"is_demo={self.is_demo}>"
        )


class Orders(Base):
    """Base orders table that identifies all orders and their status."""

    __tablename__ = "orders"
    account = Column(String, ForeignKey("users.account"))
    date = Column(DateTime, nullable=False, default=False)
    order_number = Column(String(50), nullable=False, primary_key=True)
    status = Column(String(50))
    cost = Column(Float)

    def __repr__(self):
        return (
            f"<Order account={self.account}, date={self.date},"
            f"order_number={self.order_number}, status={self.status}, cost={self.cost}>"
        )


Users.__table__.create(bind=db, checkfirst=True)
Orders.__table__.create(bind=db, checkfirst=True)
