from demo.main import export_records


def test_export_data(integration_database):
    # Check to see our export function works.
    assert export_records("users") == [
        {"account": "demo@elementhuman.com", "active": True, "is_demo": True}
    ]

    # TODO Add removal of user account as it blocks the next run of the test!

