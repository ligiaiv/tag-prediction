from predictor.source.models.model import Model
from predictor.source.dataset_management.bert_preprocessor import BertPreprocessor
from transformers import AutoModelForSequenceClassification
from predictor.source.dataset_management.dataset import Dataset
import numpy as np


class BertModel(Model):
    def __init__(self, data) -> None:
        super().__init__()
        self.dataset = Dataset(data, BertPreprocessor())

    def _proprocess_dataset():
        pass

    def train(self, dataset) -> Model:
        classes = self.preprocessor.get_classes(dataset=dataset)
        model = AutoModelForSequenceClassification.from_pretrained(
            "google-bert/bert-base-cased", num_labels=classes.len)

    def test() -> np.ndarray:
        pass
