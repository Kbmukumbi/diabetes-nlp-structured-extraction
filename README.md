# 🏥 Diabetes Clinical Notes – Structured Extraction Pipeline  
**SAT 5141 – Final Research Project**

**Authors:**  
- Kudakwashe Blessing Mukumbi  
- Zixin Shi  

---

## 📌 Overview

This repository contains an **end-to-end NLP pipeline** for extracting **structured information from diabetes-related clinical notes**.  
The project combines:

- **MIMIC-IV hospital data** (for preprocessing and generating clean discharge summaries)  
- **Kaggle I2B2 Relation Extraction JSONL dataset** (for supervised relation extraction training)

The goal is to demonstrate a complete workflow integrating **data preprocessing, text extraction, cleaning, model training, evaluation, and end-to-end inference**.

---

## 📁 Repository Structure

├── data/
│ ├── prompt1.jsonl # Kaggle I2B2 relation extraction dataset
│ ├── MIMIC dataset description.md # Dataset explanation
│
├── notebooks/
│ ├── 1_mimic_preprocessing.ipynb # MIMIC-IV preprocessing steps
│ ├── 1_mimic_preprocessing.md
│ ├── 2_kaggle_i2b2_relation_training.md
│ ├── 3_evaluation_and_examples.md
│ ├── 4_end_to_end_pipeline_demo.ipynb # Full training + inference demo
│
├── Project/ # Saved models, outputs, figures
│
├── requirements.txt
├── LICENSE
└── README.md

---

## 📦 Datasets

### **1. MIMIC-IV Structured Data (Not Included in Repo)**  
Due to privacy restrictions, MIMIC-IV files must be downloaded from PhysioNet separately.

Used tables:

- `admissions.csv`  
- `patients.csv`  
- `diagnoses_icd.csv`  
- `prescriptions.csv`  
- `discharge.csv`

Purpose:

- Identify diabetes patients (ICD-10: E10–E14)  
- Extract and merge discharge notes  
- Prepare clean clinical text for model input  

---

### **2. Kaggle I2B2 Relation Extraction Dataset**
**File in repo:** `data/prompt1.jsonl`

This JSONL dataset contains instruction-style examples for relations such as:

- *treatment improves problem*  
- *test reveals problem*  
- *problem causes problem*  

Used to fine-tune the relation extraction model.

---

## ⚙️ Installation

Install all dependencies:

```bash
pip install -r requirements.txt
Notebook 1: MIMIC Preprocessing

Location:

notebooks/1_mimic_preprocessing.ipynb


This notebook:

Loads MIMIC structured datasets

Filters diabetes patients

Extracts discharge notes

Cleans and merges text

Saves:

diabetes_patients_info.csv

diabetes_patient_notes_raw.csv
Notebook 4: Model Training + End-to-End Pipeline

Location:

notebooks/4_end_to_end_pipeline_demo.ipynb


Includes:

Loading Kaggle JSONL dataset

Tokenization

Model fine-tuning

Confusion matrix + evaluation metrics

Prediction examples

Saving the trained model
Evaluation

Metrics produced:

Accuracy

Precision

Recall

F1-score

Confusion matrix

Evaluation notebook:

notebooks/3_evaluation_and_examples.md
End-to-End Inference Demo

Example output:

{
  "problem": "diabetic neuropathy",
  "test": "nerve conduction test",
  "treatment": "gabapentin",
  "relation": "treatment_improves_problem"
}
Citations
Johnson, A. et al. (2023). MIMIC-IV.
Uzuner, Ö. et al. (2010). I2B2/VA Challenge on Concepts and Relations.
Kaggle: tomaramani, "I2B2 dataset for relation extraction".

License

MIT License


