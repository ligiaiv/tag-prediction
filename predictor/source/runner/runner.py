from dataset_management.reader import read_dataset
from dataset_management.splitter import split_dataset
from definitions import USED_MODEL, DATASET_FILENAME
from models.models import Model

if __name__ == "__main__":
    dataset = read_dataset(DATASET_FILENAME)
    dataset_splits = split_dataset(dataset)

    if issubclass(USED_MODEL, Model):
        raise Exception("Model defined in 'definitions.py' is not valid")

    model = USED_MODEL

    model.train(dataset_splits.train)
    model.test(dataset_splits.test)
