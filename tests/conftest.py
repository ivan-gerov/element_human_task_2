import logging
import os

import pytest  # type: ignore
from demo import models

log = logging.getLogger(__name__)


@pytest.fixture()
def integration_database(caplog, request, postgresql):
    caplog.set_level(logging.DEBUG)
    test_url = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(
        user=postgresql.info.user,
        password=postgresql.info.password,
        host=postgresql.info.host,
        port=postgresql.info.port,
        dbname=postgresql.info.dbname,
    )
    # Export this so we can fetch it from tests.
    os.environ["TEST_DB_URL"] = test_url
    log.debug("Generated Postgres URL %r.", test_url)

    models.metadata.create_all(models.db.engine)

    with models.session_scope() as session:
        # Add a dummy record.
        demo_user = models.Users(
            account="demo@elementhuman.com", active=True, is_demo=True
        )
        session.add(demo_user)
        session.commit()
