Diabetes Clinical Notes – Structured Extraction Pipeline

SAT 5141 – Final Research Project
Authors: Kudakwashe Blessing Mukumbi, Zixin Shi
📌 Project Overview

This project implements an end-to-end NLP pipeline for transforming unstructured diabetes clinical notes into structured, analyzable, and interoperable data.
The system combines:

ClinicalBERT fine-tuning for medication Named Entity Recognition (NER)

Relation Extraction (RE) for identifying clinical relationships such as Drug–Dose, Drug–Frequency, Drug–Route, Duration–Drug, and ADE–Drug

Weak supervision + rule-based normalization

Temporal normalization

Structured output generation for clinical decision support and diabetes research

The pipeline works on:

MIMIC-IV real-world clinical notes (unlabeled; used for context + final demo)

Kaggle i2b2 Medication Relation Dataset (labeled; used for model training & evaluation)

Repository Structure
diabetes-nlp-structured-extraction/
│
├── data/  
│   ├── discharge.csv (not uploaded due to PHI; stored locally)
│   ├── diabetes_discharge_20k/ (segmented; not uploaded)
│
├── figures/
│   ├── training_loss_curve.png
│   ├── evaluation_metrics_bar.png
│   ├── confusion_matrix.png
│
├── results/
│   ├── results_summary.md
│   ├── sample_predictions.txt
│
├── notebooks/
│   ├── preprocessing.ipynb
│   ├── model_training_end_to_end_demo.ipynb
│
├── src/
│   ├── evaluate.py
│   ├── inference.py
│
├── presentation/
│   ├── Final_Presentation.pdf  (or link)
│
├── videos/
│   ├── demo_video_link.txt
│
├── requirements.txt  
├── README.md  
└── LICENSE
Background & Motivation

Diabetes clinical notes contain critical information about:

A1c history

Insulin use

Complications

Medication changes

Hypoglycemia episodes

Lab-value–medication relationships

However, notes are unstructured, making them hard to search, summarize, or use for decision support.

Our pipeline revives Dr. Lawrence Weed’s POMR vision, converting narrative text into computable medical records using modern NLP.

Datasets Used
1. MIMIC-IV Diabetes Notes (Unlabeled)

Used for context, preprocessing, and final real-note demonstration.

18,618 diabetes-related clinical notes

~3,000 unique patients

Filtered for terms like A1c, glucose, insulin, metformin, neuropathy

Provides realistic clinical context for algorithm evaluation

2. Kaggle i2b2 Medication Relation Dataset (Labeled)

Used for training ClinicalBERT and evaluating performance.

36,348 annotated text snippets

8 relation labels

Train/Val/Test split: 30,000 / 1,000 / 5,453

Very high-quality clinical annotations
Pipeline Description
1. Preprocessing

Inserted [SUBJ]…[/SUBJ] and [OBJ]…[/OBJ] markers

Converted annotation JSON to text and numeric labels

Cleaned rows, standardized formats

Tokenized text with Bio_ClinicalBERT tokenizer

2. Model Training

Fine-tuned Bio_ClinicalBERT for relation extraction

Hyperparameters:

LR = 2e-5

Batch size = 16

Epochs = 3

Training loss steadily decreased (see figures)

3. Evaluation

✔ Loss, accuracy, precision, recall, and F1
✔ Confusion matrix
✔ Validation vs Test comparison

Test performance:
| Metric    | Value |
| --------- | ----- |
| Precision | ~0.94 |
| Recall    | ~0.94 |
| F1-score  | ~0.94 |
| Accuracy  | ~0.94 |
4. Inference & Application

Built predict_relation() function

Supports extraction from real MIMIC-IV notes

Example output:
Medication: Budesonide
Extracted Relation: Dosage–Drug
Original Text: “Budesonide 0.25 mg/2 mL solution...”
Results Summary

Stored in results/results_summary.md

Includes:

Training loss curve

Validation vs test metrics

Precision/recall/F1 bar chart

Full confusion matrix

Sample predictions on real diabetes notes

How to Run the Code
1. Install dependencies
pip install -r requirements.txt

2. Open the notebook
notebooks/model_training_end_to_end_demo.ipynb

3. Run preprocessing
python src/preprocess.py   # if included

4. Train the model

Run the training cells in the notebook.

5. Run Evaluation
python src/evaluate.py

6. Predict on new text
from src.inference import predict_relation
predict_relation("Metformin 500 mg BID was started yesterday.")
upporting Resources

Slides: The complete slide deck for the final presentation is located in the /presentation folder

 Video:https://youtu.be/VcHF8am9zPA 

Datasets:

Kaggle i2b2: https://www.kaggle.com/datasets

MIMIC-IV access via PhysioNet (not uploaded to repo due to PHI)
