import pytest
import pandas as pd
from predictor.source.dataset_management.reader import read_dataset


def test_can_read_datasets():

    DATASET_FIELDS = ["title", "description", "tags", "id"]

    dataset = read_dataset("dataset.json")
    assert (isinstance(dataset, pd.DataFrame))
    assert (len(dataset) > 0)
    print(dataset.columns)
    assert (dataset.columns.to_list() == DATASET_FIELDS)
