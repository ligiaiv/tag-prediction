import pytest
import pandas as pd
from predictor.source.models.bert import BertModel


def test_can_create_model():
    model = BertModel()
    assert (1 == 1)
