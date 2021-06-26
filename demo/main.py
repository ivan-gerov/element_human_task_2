"""Application main module."""
from typing import Any, Dict, List

from demo.models import metadata, Users, session_scope, Orders


def load_records(records: List[Dict[str, Any]]):
    """Loads records into database

    Args:
        A list of dicts containing the records.

    Returns:
        None 

    """
    with session_scope() as session:
        for record in records:
            row = Orders(**record)
            session.add(row)
        session.commit()


def export_records() -> List[Dict[str, Any]]:
    """Export records from database.

    Args:
        None

    Returns:
        A List of Dictionary objects containing the required fields.

    """
    with session_scope() as session:
        records = session.query(Orders).all()
        # Convert to a list of dictionaries.
        return [
            {
                "account": record.account,
                "date": record.date,
                "order_number": record.order_number,
                "status": record.status,
                "cost": record.cost,
            }
            for record in records
        ]
