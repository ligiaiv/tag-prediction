from dataset_management.preprocessing import Preprocessor
from transformers import AutoTokenizer


class BertPreprocessor(Preprocessor):
    def __init__(self) -> None:
        super().__init__()

        self.tokenizer = AutoTokenizer.from_pretrained(
            "google-bert/bert-base-cased")

    def preprocess_dataset(self, dataset):
        tokenized_datasets = dataset.map(self.tokenize_function, batched=True)

    def tokenize_function(self, examples):
        return self.tokenizer(examples["text"], padding="max_length", truncation=True)
