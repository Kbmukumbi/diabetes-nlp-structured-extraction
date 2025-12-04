MIMIC-IV Dataset (Used for Unlabeled Diabetes Notes)

This project uses MIMIC-IV clinical notes (PhysioNet credentialed access) to extract a subset of diabetes-related discharge summaries.

Dataset Source

MIMIC-IV v2.2
PhysioNet: https://physionet.org/content/mimiciv/2.2/

Subset Used

20,000 diabetes-related clinical notes

Extracted using keywords: “A1c”, “glucose”, “diabetes”, “insulin”, “neuropathy”, “metformin”, etc.

Notes were preprocessed (cleaning, PHI removal, tokenization, sectioning)

Important

The raw MIMIC dataset cannot be uploaded to GitHub due to privacy and licensing restrictions.
Only derived features, cleaned notes (non-PHI), and pipeline outputs are shared in this repository.
