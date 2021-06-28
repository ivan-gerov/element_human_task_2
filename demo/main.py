"""Application main module."""
from typing import Any, Dict, List

from demo.models import metadata, session_scope, Users, Orders
from demo.utils import get_table_records

from datetime import datetime, timedelta
from sqlalchemy import extract, func
from sqlalchemy.exc import IntegrityError


def load_records(orders: List[Dict[str, Any]]):
    """Loads order records into database into the Orders Table
    and add a new User per new unique user email.

    Args:
        A list of dicts containing the orders and 
        the table in which we want to import them.

    Returns:
        None 

    """
    with session_scope() as session:
        for record in orders:
            try:
                users = [user["account"] for user in get_table_records(Users)]
                if record["account"] not in users:
                    user = {
                        "account": record["account"],
                        "active": True,
                        "is_demo": True,
                    }
                    row = Users(**user)
                    session.add(row)
                    session.commit()
            except IntegrityError:
                print("User is already in the database")

            try:
                orders = [order["order_number"] for order in get_table_records(Orders)]
                row = Orders(**record)
                session.add(row)
                session.commit()
            except IntegrityError:
                print("Order is already in the database")


def export_records() -> List[Dict[str, Any]]:
    """Export users accounts and total account value for the past 12 months.

    Args:
        None

    Returns:
        A List of Dictionary objects containing the required fields.

    """
    return_val = []
    with session_scope() as session:
        filter_after = datetime.today() - timedelta(12 * 30)

        records = (
            session.query(Users, func.sum(Orders.cost).label("total_account_value"))
            .join(Orders)
            .filter(
                extract("year", Orders.date) >= filter_after.year,
                extract("month", Orders.date) >= filter_after.month,
                extract("day", Orders.date) >= filter_after.day,
            )
            .group_by(Users.account)
            .all()
        )

        for user_account, total_account_value in records:
            user_account = {
                "account": user_account.account,
                "active": user_account.active,
                "is_demo": user_account.is_demo,
                "total_account_value": total_account_value,
            }
            return_val.append(user_account)
    return return_val
