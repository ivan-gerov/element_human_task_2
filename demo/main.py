"""Application main module."""
from typing import Any, Dict, List

from demo.models import metadata, Users, session_scope, Orders
from demo.utils import get_table_records

from sqlalchemy.exc import IntegrityError

def load_records(orders: List[Dict[str, Any]]):
    """Loads order records into database

    Args:
        A list of dicts containing the orders and 
        the table in which we want to import them.

    Returns:
        None 

    """
    tables = {"orders": Orders, "users": Users}
    with session_scope() as session:
        for record in orders:
            try:
                users = [user["account"] for user in get_table_records(tables["users"])] 
                if record["account"] not in users:                    
                    user = {
                        "account": record["account"],
                        "active": True,
                        "is_demo": True
                        }
                    row = tables["users"](**user)
                    session.add(row)
                    session.commit()
            except IntegrityError:
                print("User is already in the database")

            try:
                orders = [order["order_number"] for order in get_table_records(tables["orders"])]
                row = tables["orders"](**record)
                session.add(row)
                session.commit()
            except Exception as e:
                print(e)
                print("Order is already in the database")


def export_records(table: str) -> List[Dict[str, Any]]:
    """Export records from database.

    Args:
        None

    Returns:
        A List of Dictionary objects containing the required fields.

    """

    
    tables = {"orders": Orders, "users": Users}

    # TODO Make a join operation that calculates what the task requires
    return return_val
