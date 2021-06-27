from demo.utils import extract_orderno_and_status, parse_orders
from pandas import Timestamp


def test_extract_orderno_and_status():
    """
    Tests the extraction of an order_number and status from
    the "data" nested json field of orders CSV files.
    """

    test_data = {
        "a": "null",
        "b": {"c": [6, 5, 4, 3]},
        "order_number": 4,
        "e": [{"status": "success"}],
    }
    processed_test_data = extract_orderno_and_status(test_data)
    assert processed_test_data == {"order_number": 4, "status": "success"}

    test_data = {
        "a": [{"b": {"c": {"order_number": 3}}}, {"e": "unknown", "status": "unknown"}]
    }
    processed_test_data = extract_orderno_and_status(test_data)
    assert processed_test_data == {"order_number": 3, "status": "unknown"}


def test_parse_orders():
    """
    Tests that parse_orders successfully parses an orders CSV file
    into a list of dict objects. 
    """
    test_filepath = "tests/resources/parse_orders_test_data.csv"
    expected_result = [
        {
            "account": "demo@elementhuman.com",
            "date": Timestamp("2020-08-16 14:20:39.031796"),
            "cost": 4.32,
            "order_number": 3,
            "status": "unknown",
        },
        {
            "account": "sam.pegler@elementhuman.com",
            "date": Timestamp("2020-08-16 14:55:15.031796"),
            "cost": 5.32,
            "order_number": 4,
            "status": "success",
        },
    ]

    assert parse_orders(test_filepath) == expected_result
