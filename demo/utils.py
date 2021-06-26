
import pandas as pd
import json



def flatten_dict(nested_dict):
    """
        Flatten dict object with nested keys into a single level.

        Args:
            nested_dict: A nested dict object.

        Returns:
            The flattened dict object if successful, None otherwise.
    """
    out = {}

    def flatten(struct, name=""):
        if type(struct) is dict:
            for item in struct:
                flatten(struct[item], item)
        else:
            out[name] = struct

    flatten(nested_dict)
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
    df = pd.read_csv(csv_filepath)

    df["data"] = df["data"].transform(lambda x: json.loads(x))
    df["data"] = df["data"].apply(lambda x: flatten_dict(x))


    list_of_parsed_rows = list(df.T.to_dict().values())

    list_of_parsed_rows
    
    return list_of_parsed_rows


filepath = "tests/resources/orders.csv"

data = parse_orders(filepath)

print(data[0])