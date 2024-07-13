import pandas as pd
import json
import os


def _dataset_checks(dataset: pd.DataFrame) -> bool:
    return True


def read_dataset(location: str) -> pd.DataFrame:
    with open("resources/" + location, 'r') as infile:
        data = json.load(infile)

    dataset = pd.DataFrame.from_dict(data["samples"])

    return dataset
