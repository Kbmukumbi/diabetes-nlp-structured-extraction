I2B2 Relation Extraction Dataset (Kaggle version)

The file prompt1.jsonl comes from the Kaggle dataset based on the I2B2 medical relation extraction challenge.

Dataset Source

Kaggle Dataset:
“I2B2 dataset for relation extraction”
https://www.kaggle.com/datasets/tomaraman/i2b2-dataset-for-relation-extraction

Dataset Format

The dataset is provided as a JSONL (JSON Lines) file, where each line includes:

instruction (task description)

context (clinical text with marked subject/object entities)

response (the expected relation)

Preprocessed NER + relation labels

What this dataset is used for

This dataset provides supervised labels for:

Training and fine-tuning ClinicalBERT for relation classification

Mapping Subject–Object pairs into relation categories such as:

Reason-Drug

Route-Drug

Strength-Drug

Frequency-Drug

Duration-Drug

Dosage-Drug

Form-Drug

ADE-Drug

Why we used it

The MIMIC-IV dataset contains unlabeled diabetes notes, therefore supervised learning is not possible without labels.

prompt1.jsonl provides:

Clean training examples

Clear relation annotations

A standard benchmark for medical NLP

This dataset enables our model to train a relation extraction classifier that can later be applied to the MIMIC diabetes notes.
