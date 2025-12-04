import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import torch
import os

MODEL_NAME = "distilroberta-base"

def load_data(train_path):
    return pd.read_csv(train_path)

def encode_dataset(df, tokenizer):
    return Dataset.from_pandas(df).map(lambda x: tokenizer(x["text"], truncation=True, padding="max_length"), batched=True)

def train_model(train_csv):
    df = load_data(train_csv)
    labels = sorted(df["relation"].unique())

    label_to_id = {label: i for i, label in enumerate(labels)}
    df["labels"] = df["relation"].map(label_to_id)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    dataset = encode_dataset(df, tokenizer)

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME,
        num_labels=len(labels)
    )

    args = TrainingArguments(
        output_dir="Project/model",
        num_train_epochs=3,
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        save_total_limit=1,
        logging_steps=20
    )

    trainer = Trainer(model=model, args=args, train_dataset=dataset)
    trainer.train()

    model.save_pretrained("Project/model")
    tokenizer.save_pretrained("Project/model")

    print("Model saved → Project/model")


if __name__ == "__main__":
    train_model("data/processed/train.csv")
