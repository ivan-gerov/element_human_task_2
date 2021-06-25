"""Test Migrations both up and down."""
import logging

from alembic.config import Config  # type: ignore
from alembic import command, script  # type: ignore
from sqlalchemy import create_engine  # type: ignore

from demo.models import Base


log = logging.getLogger(__name__)


def test_migrations(caplog, postgresql):
    caplog.set_level(logging.DEBUG)
    db_url = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(
        user=postgresql.info.user,
        password=postgresql.info.password,
        host=postgresql.info.host,
        port=postgresql.info.port,
        dbname=postgresql.info.dbname,
    )
    log.info("Analytics url for test is %r", db_url)

    # Build the database as to current models.
    db = create_engine(db_url)
    Base.metadata.create_all(db)

    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", "migrations")
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)

    directory = script.ScriptDirectory.from_config(alembic_cfg)
    log.info("Current head is %r", directory.get_heads())

    # This sets where we are as the current HEAD and sets up the table.
    log.info("Stamping as current version.")
    command.stamp(alembic_cfg, "head")

    # Migrate all the way back to the past; then fast forward back to now.
    # This ensures that we can both upgrade and downgrade in all directions.
    log.debug("Attempting to downgrade to base.")
    command.downgrade(alembic_cfg, "base")
    log.info("Succesfully downgraded to base.")

    log.debug("Attempting to upgrade to head.")
    command.upgrade(alembic_cfg, "head")
    log.debug("Succesfully upgraded to head.")
