from predictor.source.dataset_management.reader import read_dataset
from predictor.source.dataset_management.splitter import split_dataset
from definitions import USED_MODEL, DATASET_FILENAME
from predictor.source.models.model import Model
from predictor.source.dataset_management.dataset import Dataset

if __name__ == "__main__":
    dataset = read_dataset(DATASET_FILENAME)
    [train_split, test_split] = split_dataset(dataset, 0.7)

    if not issubclass(USED_MODEL, Model):
        raise Exception("Model defined in 'definitions.py' is not valid")

    model = USED_MODEL(train_split)

    model.train()
    model.test(test_split)
