import json
import pandas as pd
from sklearn.model_selection import train_test_split

def load_i2b2_jsonl(jsonl_path):
    """Load Kaggle I2B2 relation extraction dataset (JSONL format)."""
    data = []
    with open(jsonl_path, "r") as f:
        for line in f:
            item = json.loads(line)
            data.append({
                "text": item.get("text", ""),
                "relation": item.get("relation", "")
            })
    return pd.DataFrame(data)


def clean_text(text):
    """Simple text cleaning logic."""
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text


def preprocess_dataframe(df):
    """Apply text cleaning to all samples."""
    df["text"] = df["text"].apply(clean_text)
    df = df[df["relation"].notna()]
    return df


def create_splits(df, test_size=0.2, seed=42):
    """Split into train and test sets."""
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=seed, stratify=df["relation"])
    return train_df, test_df


def save_processed(train_df, test_df, output_dir="data/processed"):
    """Save final train/test CSV."""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    train_df.to_csv(f"{output_dir}/train.csv", index=False)
    test_df.to_csv(f"{output_dir}/test.csv", index=False)
    print("Saved processed data →", output_dir)


if __name__ == "__main__":
    # Example pipeline run
    df = load_i2b2_jsonl("data/prompt1.jsonl")
    df = preprocess_dataframe(df)
    train_df, test_df = create_splits(df)
    save_processed(train_df, test_df)
