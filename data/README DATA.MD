# Data Notes

This repository does **not** contain any raw clinical text.

For this project we used:
- De-identified clinical notes (e.g., from MIMIC-IV).
- Optionally synthetic notes generated with Synthea.

If you want to run the notebook:

1. Obtain appropriate access to a de-identified clinical notes dataset
   (for example, MIMIC-IV from PhysioNet).
2. Store the CSV or text files locally or on Google Drive.
3. Update the paths in `notebooks/diabetes_ner_pipeline.ipynb`
   (e.g., `CSV_PATH = "/content/drive/MyDrive/diabetes_patient_notes_clean.csv"`).

