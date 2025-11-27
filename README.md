# Diabetes NLP Structured Extraction

**Course project – Natural Language Processing in Biomedicine**  
Michigan Technological University  
**Authors:** Kudakwashe Blessing Mukumbi & Zixin Shi

---

## 📌 Project Overview

Clinical notes contain rich but messy information about diabetes care:
- Lab results (e.g., *HbA1c, glucose, eGFR*)
- Medications (e.g., *metformin, insulin, SGLT2i*)
- Complications and comorbidities (e.g., *neuropathy, CKD, CAD*)

Most of this lives in **free text**, which is hard to use for:
- Longitudinal tracking of glycemic control  
- Clinical decision support (CDSS)  
- Research and quality improvement  

This project builds a **diabetes-focused NLP pipeline** that transforms free-text clinical notes into **structured, interoperable data**.

We combine:
- **Weakly supervised labeling rules** (regex + heuristics)
- **ClinicalBERT** fine-tuning for token-level NER
- Simple **relation/slot extraction** to connect:
  - `LABTEST` ↔ `LABVALUE` ↔ `UNIT` ↔ `DATE`

The focus is on *diabetes-relevant entities* and *timeline reconstruction*.

---

## 🎯 Goals

1. **Extract diabetes-related entities** from notes  
   - Lab tests (e.g., HbA1c, fasting glucose)  
   - Lab values + units  
   - Time expressions / dates  
   - Diabetes medications and complications (future extension)

2. **Link entities together**  
   - Example: turn  
     > “HbA1c 9.6% in June 2024”  
     into a structured record with test, value, unit, and normalized date.

3. **Normalize concepts**  
   - Map lab tests and drugs to standard vocabularies where possible  
     (LOINC, RxNorm, SNOMED) to support interoperability.

4. **Generate structured outputs**  
   - Token-level BIO tags (NER)  
   - Simple JSON / table views for each note that can be plugged into  
     CDSS pipelines or downstream analytics.

---

## 🧱 Repository Contents

- `notebooks/diabetes_ner_pipeline.ipynb`  
  End-to-end Colab notebook:
  - Load and clean clinical notes  
  - Build weak labels with simple regex + rules  
  - Prepare a token-level dataset (`df_ner`)  
  - Fine-tune **Bio_ClinicalBERT** with HuggingFace `Trainer`  
  - Evaluate on a held-out dev split  
  - Quick inference demo on new notes

- `requirements.txt`  
  Python dependencies used in the notebook.

- `docs/project_proposal.pdf`  
  Short proposal describing the motivation, literature, and methodology.

- `docs/methodology_summary.md`  
  One-page summary of the pipeline and how it connects to diabetes use cases.

- `data/README_DATA.md`  
  Notes about data sources (e.g., MIMIC-IV, Synthea) and access restrictions.
  **No raw clinical data is stored in this repository.**

---

## 🧬 Methods (High-Level)

1. **Data**
   - De-identified clinical notes (e.g., discharge summaries).
   - Focus on notes containing diabetes-related keywords.

2. **Pre-processing**
   - Basic cleaning (whitespace, headers, de-identification tokens).
   - Keep both raw text and a lightly cleaned version (`clean_text`).

3. **Weak Labeling (Option 3 in our proposal)**
   - Tokenize into simple space-separated tokens.
   - Apply regex + heuristics to assign BIO tags for:
     - `LABTEST`, `LABVALUE`, `UNIT`, `DATE`
   - Everything else is labeled `O`.
   - This produces a weakly-labeled dataframe: `df_ner` with
     `tokens` and `labels` lists per note.

4. **Model**
   - Base model: `emilyalsentzer/Bio_ClinicalBERT`
   - Task: token classification (NER) with 9 labels:  
     `['O', 'B-LABTEST', 'I-LABTEST', 'B-LABVALUE', 'I-LABVALUE',
       'B-UNIT', 'I-UNIT', 'B-DATE', 'I-DATE']`
   - Implementation: HuggingFace `transformers` + `datasets`.

5. **Training & Evaluation**
   - Split into train / validation.
   - Fine-tune for 1–2 epochs (CPU-friendly for Colab).
   - Metrics: token-level accuracy (and F1 where needed).

6. **Inference**
   - Simple helper function to:
     - Take raw note text
     - Run tokenization + model
     - Return predicted spans for LABTEST, LABVALUE, UNIT, DATE.

---

## ⚙️ How to Run (Colab-Friendly)

1. **Clone the repo**

```bash
pip install -r requirements.txt
pip install -r requirements.txt


git clone https://github.com/Kbmukumbi/diabetes-nlp-structured-extraction.git
cd diabetes-nlp-structured-extraction
