# Notebook 02 — Relation Extraction Training (I2B2 Dataset)

This notebook trains a ClinicalBERT-based classifier using the processed I2B2 relation dataset from Kaggle (`prompt1.jsonl`).

Steps covered:
- Load and convert `prompt1.jsonl` to a clean DataFrame
- Extract text + relation labels
- Split into train/validation/test sets
- Tokenize using Bio_ClinicalBERT
- Train a multi-class classifier on 8 relation types:
  - ADE-Drug
  - Dosage-Drug
  - Duration-Drug
  - Form-Drug
  - Frequency-Drug
  - Reason-Drug
  - Route-Drug
  - Strength-Drug
- Evaluate on validation and test sets (accuracy, precision, recall, F1)
