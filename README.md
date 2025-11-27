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
## NER Pipeline Evaluation

We trained a weakly supervised NER model to tag diabetes-relevant entities in
clinical notes (LABTEST, LABVALUE, UNIT, DATE).

**Setup**

- Dataset: 18,618 de-identified discharge summaries (MIMIC dev notes).
- Labels: Weak IOB tags generated with simple regex + heuristic rules.
- Split: 80% train / 20% validation on the weakly labelled notes.
- Model: `emilyalsentzer/Bio_ClinicalBERT` fine-tuned for 1 epoch using
  HuggingFace `Trainer` (CPU-friendly, small batch size).

**Validation results**

- Token-level accuracy: **0.9996**
- Validation loss: **0.0028**
- Most tokens are “O”, so accuracy is dominated by background text, but
  spot-checks show the model is able to pick up numeric lab values and some
  diabetes-related terms.

**Take-aways**

- A simple weak-labeling strategy + one-epoch fine-tuning is enough to get a
  working proof-of-concept NER model for diabetes notes.
- The current model is intended as a baseline; future work includes:
  - Better labeling rules for LABTEST / UNIT / DATE.
  - Entity-level precision/recall/F1 using a manually annotated subset.
  - Stronger relation extraction between LABTEST–LABVALUE–UNIT–DATE.


## ⚙️ How to Run (Colab-Friendly)

1. **Clone the repo**

```bash
pip install -r requirements.txt
pip install -r requirements.txt


git clone https://github.com/Kbmukumbi/diabetes-nlp-structured-extraction.git
cd diabetes-nlp-structured-extraction

## 🔍 Evaluation & Key Findings

We trained a token-level NER model by fine-tuning **Bio_ClinicalBERT** on the weakly labeled notes (`df_ner`).

**Setup**

- Base model: `emilyalsentzer/Bio_ClinicalBERT`
- Labels: `O`, `B/I-LABTEST`, `B/I-LABVALUE`, `B/I-UNIT`, `B/I-DATE`
- Train/validation split: 80% / 20% of 18,618 notes
- Epochs: 1 (Colab-friendly)
- Batch size: 4 (CPU)
- Optimizer and scheduler: default HuggingFace `Trainer` settings

**Token-level metrics (validation set)**

- Loss: **≈ 0.0028**
- Accuracy: **≈ 0.9996**

Because labels are generated with simple rules, accuracy is mostly measuring **how well the model reproduces our weak labels**. The important result is that Bio_ClinicalBERT can:

- Learn the **pattern of lab expressions** (e.g., “HbA1c 8.9 %”, “glucose 140 mg/dL 06/2024”).
- Generalize to similar expressions in **previously unseen notes**.

**Qualitative examples**

On held-out notes, the model correctly tags:

- `HbA1c` as **LABTEST**, `8.9` as **LABVALUE**, `%` as **UNIT**, and `06/2024` as **DATE**.
- Fasting glucose measurements with varying formats, such as  
  `glucose 140`, `glu 95`, or `blood sugar 210 mg/dL`.

These token-level spans are then fed into a simple rule-based linker to reconstruct **structured diabetes events** like:

> “A1c = 8.9 % on 2024-06-15”

---

## 👥 Target Population & Clinical Impact

**Target population**

Hospitalized / ICU patients with **diabetes and related cardiometabolic disease** documented in MIMIC-IV–style clinical notes.

**Why this matters**

- Diabetes patients often have **long, complex EHR histories**, with critical details scattered across years of notes.
- Key decisions (e.g., intensifying insulin, adding SGLT2 inhibitors) depend on understanding **trends** in HbA1c and related labs, not just the most recent value.
- Many clinical decision support systems **ignore free text**, so diabetes-relevant information is effectively “invisible” to algorithms.

**Potential impact**

This prototype demonstrates how an NLP pipeline can:

- Turn free-text ICU notes into **structured lab timelines** (LABTEST, LABVALUE, UNIT, DATE).
- Reduce the cognitive load for clinicians who need a **quick, accurate picture of glycemic control**.
- Provide **structured features** that can be plugged into:
  - CDSS alerts for poor glycemic control or hypoglycemia risk.
  - Disease progression models for diabetes complications.
  - Quality-improvement dashboards on diabetes management.

While this is an early, weakly supervised system, it shows a realistic path from **messy narrative text** to **interoperable diabetes data** that can benefit both clinicians and patients.
