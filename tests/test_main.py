from demo.main import export_records


def test_export_data(integration_database):
    """Checks if test data can be sucessfully exported from database."""
    assert export_records("users") == [
        {"account": "demo@elementhuman.com", "active": True, "is_demo": True}
    ]
