from predictor.source.dataset_management.bert_preprocessor import BertPreprocessor
from predictor.source.models.model import Model
from predictor.source.dataset_management.dataset import Dataset

class LinearRegressionModel(Model):
    def __init__(self, data) -> None:
        self.dataset = Dataset(data, BertPreprocessor())
        # self.model =

    def train(self):
        pass

