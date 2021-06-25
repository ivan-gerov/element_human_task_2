"""Application main module."""
from typing import Any, Dict, List

from demo.models import metadata, Users, session_scope


def export_records() -> List[Dict[str, Any]]:
    """Export records from database.

    Args:
        None

    Returns:
        A List of Dictionary objects containing the required fields.

    """
    with session_scope() as session:
        records = session.query(Users).all()
        # Convert to a list of dictionaries.
        return [
            {
                "account": record.account,
                "active": record.active,
                "is_demo": record.is_demo,
            }
            for record in records
        ]
