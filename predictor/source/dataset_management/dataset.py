import itertools

import pandas as pd


class Dataset:
    def __init__(self, raw_data: pd.DataFrame, preprocessor) -> None:
        self.preprocessor = preprocessor
        self.raw_data = raw_data
        self.classes = []
        self.id2class = {}
        self.class2id = {}
        self.train_dataset = []
        self.test_dataset = []
        self._create_dictionaries(raw_data['tags'])

    def _create_dictionaries(self, tags_column):
        self.classes = list(itertools.chain.from_iterable(tags_column))
        self.class2id = {class_: id for id, class_ in enumerate(self.classes)}
        self.id2class = {id: class_ for class_, id in self.class2id.items()}
