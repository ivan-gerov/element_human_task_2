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


def export_records(table) -> List[Dict[str, Any]]:
    """Export records from database.

    Args:
        None

    Returns:
        A List of Dictionary objects containing the required fields.

    """
    with session_scope() as session:
        if table == "orders":
            records = session.query(Orders).all()
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
        elif table == "users":
            records = session.query(Users).all()
            return [
                {
                    "account": record.account,
                    "active": record.active,
                    "is_demo": record.is_demo,
                }
                for record in records
            ]

