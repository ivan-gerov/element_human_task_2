"""Application cli module."""
import csv
import logging
import os
from glob import glob

import click  # type: ignore

from demo.main import export_records, load_records
from demo.utils import parse_orders


log = logging.getLogger(__name__)


@click.group()
def cli():
    """Click group used to tie commands together."""
    # Setup the standard stream handler to write to stdout
    logging.basicConfig(level=os.environ.get("PIPELINE_LOG_LEVEL", "INFO").upper())


@cli.command()
@click.option(
    "--filepath", required=True, help="Path to files to index. Supports globbing."
)
def load(filepath):
    """Command line interface to load data to our database.

    Args:
        filepath (str): Path to file to parse and upload.

    Returns:
        None

    """
    log.info("Loading files.")

    orders = parse_orders(filepath)
    load_records(orders)


@cli.command()
@click.option("--filepath", required=True, help="Path to write records to.")
@click.option("--db_table", required=True, help="Path to write records to.")
def export(filepath, db_table):  # pragma: no cover
    """Export database records to CSV at file path."""
    log.info("Exporting records to file.")

    # Fetch records to export and get a list of fields to export.
    exportable_records = export_records(db_table)
    fieldnames = list(exportable_records[0].keys())

    log.info("Exporting %r columns over %r rows.", fieldnames, len(exportable_records))
    with open(filepath, "w") as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in exportable_records:
            writer.writerow(row)

    log.info("Export complete.")
