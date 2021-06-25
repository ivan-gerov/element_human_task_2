from demo.main import export_records


def test_export_data(integration_database):
    # Check to see our export function works.
    assert export_records() == [
        {"account": "demo@elementhuman.com", "active": True, "is_demo": True}
    ]
