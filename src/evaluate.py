import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.metrics import classification_report, confusion_matrix
import torch
import json
import os

MODEL_DIR = "Project/model"

def load_data(path):
    return pd.read_csv(path)

def predict(df):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)

    preds = []
    for text in df["text"]:
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            logits = model(**inputs).logits
        pred = torch.argmax(logits, dim=1).item()
        preds.append(pred)

    return preds

def evaluate(test_csv):
    df = load_data(test_csv)
    
    label_list = sorted(df["relation"].unique())
    label_to_id = {label: i for i, label in enumerate(label_list)}
    df["true"] = df["relation"].map(label_to_id)

    df["pred"] = predict(df)

    report = classification_report(df["true"], df["pred"], target_names=label_list, output_dict=True)
    cm = confusion_matrix(df["true"], df["pred"])

    os.makedirs("results", exist_ok=True)

    with open("results/classification_report.txt", "w") as f:
        f.write(classification_report(df["true"], df["pred"], target_names=label_list))

    with open("results/final_metrics.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Saved evaluation results → results/")
    print("Confusion Matrix:\n", cm)


if __name__ == "__main__":
    evaluate("data/processed/test.csv")
