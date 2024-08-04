import numpy as np
import pandas as pd
from typing import List


class Preprocessor():
    def __init__(self) -> None:
        pass

    def preprocess_dataset(self, dataset: pd.DataFrame):
        pass

    def get_classes(self, dataset: pd.DataFrame) -> List[str]:
        return dataset["tags"].unique().tolist()
