import logging
import os
import sys
import tempfile

import pytest  # type: ignore
from demo.models import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pytest_postgresql import factories

log = logging.getLogger(__name__)

socket_dir = tempfile.TemporaryDirectory()
postgresql_my_proc = factories.postgresql_proc(
    port=None, unixsocketdir=socket_dir.name)
postgresql_my = factories.postgresql("postgresql_my_proc")

@pytest.fixture(scope="function")
def integration_database(caplog, request, postgresql_my):
    caplog.set_level(logging.DEBUG)

    def dbcreator():
        return postgresql_my.cursor().connection

    db = create_engine("postgresql+psycopg2://", creator=dbcreator)
    Base.metadata.create_all(db)

    Session = sessionmaker(bind=db)
    session = Session()
    yield session
    session.close()


