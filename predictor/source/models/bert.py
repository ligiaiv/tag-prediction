from predictor.source.models.compute_metrics import compute_metrics
from predictor.source.dataset_management.splitter import split_dataset
from predictor.source.models.model import Model
from predictor.source.dataset_management.bert_preprocessor import BertPreprocessor
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer, \
    DataCollatorWithPadding
from predictor.source.dataset_management.dataset import Dataset
import numpy as np


class BertModel(Model):
    def __init__(self, data) -> None:
        super().__init__()
        self.dataset = Dataset(data, BertPreprocessor())
        self.classes = self.dataset.classes
        self.model = None
        self.tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")
        self.tokenized_dataset = self.dataset.raw_data.apply(self._proprocess_dataset, axis=1)

    def _proprocess_dataset(self, sample):
        text = f"{sample['title']}.\n{sample['description']}"
        all_labels = sample['tags']
        labels = [0. for i in range(len(self.classes))]
        for label in all_labels:
            label_id = self.dataset.class2id[label]
            labels[label_id] = 1.

        sample = self.tokenizer(text, truncation=True)
        sample['labels'] = labels
        return sample

    def train(self) -> Model:
        classes = self.dataset.classes
        print(len(self.dataset.id2class), len(classes), len(self.dataset.class2id))
        model = AutoModelForSequenceClassification.from_pretrained("google-bert/bert-base-cased",
                                                                    num_labels=len(classes),
                                                                    id2label=self.dataset.id2class,
                                                                    label2id=self.dataset.class2id,
                                                                    problem_type = "multi_label_classification")

        training_args = TrainingArguments(

            output_dir="my_awesome_model",
            learning_rate=2e-5,
            per_device_train_batch_size=3,
            per_device_eval_batch_size=3,
            num_train_epochs=2,
            weight_decay=0.01,
            evaluation_strategy="epoch",
            save_strategy="epoch",
            load_best_model_at_end=True,
        )
        [train_data, val_data] = split_dataset(self.tokenized_dataset, 0.85)
        data_collator = DataCollatorWithPadding(tokenizer=self.tokenizer)

        trainer = Trainer(
            model = model,
            args= training_args,
            train_dataset= train_data,
            eval_dataset= val_data,
            tokenizer= self.tokenizer,
            data_collator= data_collator,
            compute_metrics= compute_metrics
        )

        trainer.train()






    def test(self, test_samples) -> np.ndarray:
        pass
