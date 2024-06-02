import pandas as pd
import json


class Dataset:

    def __init__(self, filename: str,  fields: dict):
        self.fields = fields
        self.filename = filename
        self.dataset = self.read_dataset()
        # self.dataset = self.dataset.astype(fields)

    def read_dataset(self) -> {}:
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {'samples': []}

    def add_samples(self, samples: []):
        self.dataset['samples'] = self.dataset['samples'] + samples
        print(len(self.dataset["samples"]), len(samples))

    def check_last_id(self):
        if len(self.dataset["samples"]) == 0:
            return 0

        return max([sample["id"] for sample in self.dataset["samples"]])

    def save_dataset(self):
        with open(self.filename, 'w') as f:
            json.dump(f, self.dataset)
