"""Application cli module."""
import csv
import logging
import os
from glob import glob

import click  # type: ignore

from demo.main import export_records


log = logging.getLogger(__name__)


@click.group()
def cli():
    """Click group used to tie commands together."""
    # Setup the standard stream handler to write to stdout
    logging.basicConfig(level=os.environ.get("PIPELINE_LOG_LEVEL", "INFO").upper())


@cli.command()
@click.option(
    "--files", required=True, help="Path to files to index. Supports globbing."
)
def load(respondent_id, notify):
    """Command line interface to load data to our database.

    Args:
        files (str): Path to files to parse and upload.

    Returns:
        None

    """
    log.info("Loading files.")

    # TODO: Implement the rest of this command line function.
    files = glob(files)
    ...


@cli.command()
@click.option("--file", required=True, help="Path to write records to.")
def export(file):  # pragma: no cover
    """Export database records to CSV at file path."""
    log.info("Exporting records to file.")

    # Fetch records to export and get a list of fields to export.
    exportable_records = export_records()
    fieldnames = list(exportable_records[0].keys())

    log.info("Exporting %r columns over %r rows.", fieldnames, len(export_records))
    with open(file, "w") as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in exportable_records:
            writer.writerow(row)

    log.info("Export complete.")
