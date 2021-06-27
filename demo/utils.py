import pandas as pd
import json
from .models import session_scope

def extract_orderno_and_status(nested_dict: dict) -> dict:
    """
        Flatten dict object with nested keys into a single level and
        extract order_number and status.

        Args:
            nested_dict: A nested dict object.

        Returns:
            The flattened dict containing order_number and status fields.
    """
    out = {}

    def flatten(struct, name=""):
        if type(struct) is dict:
            for item in struct:
                flatten(struct[item], item)
        elif type(struct) is list:
            i = 0
            for item in struct:
                flatten(item, str(i))
                i += 1
        else:
            out[name] = struct

    flatten(nested_dict)

    out = {k: v for k, v in out.items() if k in ["status", "order_number"]}

    return out


def parse_orders(csv_filepath: str) -> list:
    """ 
        Parses Orders CSV file contents to a list of dicts, where
        each dict is a table row of with fields:
             account, date, order_number, status, cost
        

        Args:
            csv: CSV file string

        Returns:
            list of dicts
    """
    # Read data in Pandas DataFrame
    df = pd.read_csv(csv_filepath)

    # Parse raw "data" field (json) and set up order_number and status fields in DataFrame
    df["data"] = df["data"].transform(lambda x: json.loads(x))
    df["data"] = df["data"].apply(lambda x: extract_orderno_and_status(x))
    df = df.join(pd.DataFrame([x for x in df["data"]]))
    df.drop(columns=["data", "products"], inplace=True)

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Convert Dataframe to a list of dicts for each row
    list_of_parsed_rows = list(df.T.to_dict().values())

    return list_of_parsed_rows

def get_table_records(table):
    rows = []
    with session_scope() as session:
        records = session.query(table).all()
        # Dynamically getting all columns and values
        for record in records:
            record = record.__dict__.copy()
            record.pop("_sa_instance_state", None)
            rows.append(record)
    return rows

