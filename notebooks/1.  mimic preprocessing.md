# Notebook 01 — MIMIC Diabetes Notes Preprocessing

This notebook performs all preprocessing for the MIMIC-IV diabetes discharge notes:
- Load 20k discharge notes
- Filter notes with diabetes-related keywords (A1c, insulin, glucose, metformin)
- Clean PHI placeholders and noise
- Normalize text (lowercase, regex cleaning)
- Segment notes into structured sections
- Save outputs:
  - `diabetes_discharge_20k_clean.csv`
  - `diabetes_discharge_20k_segmented.pkl`

These cleaned files are used later for downstream structured extraction.
