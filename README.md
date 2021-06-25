# Demo ETL Pipeline

This is a demo ETL pipeline that that merges hypothetical data with existing
records.


### Installation

The setup requires Python3.6 or above and the installation instructions are
written to be run inside of a virtual environment.

```sh
# Production installation that just contains dependency packages.
python setup.py install
# Development installation that brings along test dependencies.
python setup.py develop
```

### Tests

Check everything works before you start.

```sh
black demo --check
pytest -vv
```

### Configuration

Configuration for the app is as follows.

| Configurable     | Info                          | Environment Variable | Default   |
|:-----------------|:------------------------------|:---------------------|:----------|
| Log Level        | Console log level             | PIPELINE_LOG_LEVEL   | INFO      |
| API Database URL | Takes a prefixed database URL | PIPELINE_DB_URL      | sqlite:// |

Pipeline database URL can either be a postgres or sqlite URL.


### Running

To run the pipeline locally using the development configuration (this has defaults)
but can be overriden with environment variables as per the configuration.

```sh
etl export --file=/tmp/export.csv
```


### Migrations

This repository uses alembic to manage SQL migrations.  One existing migration
is included.

```sh
# Create a new revison.
alembic revision
```

To test your migrations are succesful we've added a test which fully downgrades
and then fully upgrades the database.

```sh
pytest tests/test_migrations.py
```
