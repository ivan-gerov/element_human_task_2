"""Application main module."""
from typing import Any, Dict, List

from demo.models import metadata, Users, session_scope, Orders


def load_records(records: List[Dict[str, Any]], table: str):
    """Loads records into database

    Args:
        A list of dicts containing the records and 
        the table in which we want to import them.

    Returns:
        None 

    """
    tables = {"orders": Orders, "users": Users}

    with session_scope() as session:
        for record in records:
            row = tables[table](**record)
            session.add(row)
        session.commit()


def export_records(table: str) -> List[Dict[str, Any]]:
    """Export records from database.

    Args:
        None

    Returns:
        A List of Dictionary objects containing the required fields.

    """

    return_val = []
    tables = {"orders": Orders, "users": Users}
    with session_scope() as session:
        rows = []
        records = session.query(tables[table]).all()
        # Dynamically getting all columns and values
        for record in records:
            record = record.__dict__.copy()
            record.pop("_sa_instance_state", None)
            return_val.append(record)

    return return_val
