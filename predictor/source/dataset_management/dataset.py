
class Dataset:
    def __init__(self, raw_data, preprocessor) -> None:
        self.preprocessor = preprocessor
        self.raw_data = raw_data
        self.classes = []
        self.id2class = {}
        self.class2id = {}
        self.train_dataset = []
        self.test_dataset = []

    def _create_dictionaries(self):
        self.class2id = {class_: id for id, class_ in enumerate(self.classes)}
        self.id2class = {id: class_ for class_, id in self.class2id.items()}
