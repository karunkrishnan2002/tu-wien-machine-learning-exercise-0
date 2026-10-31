# TU Wien — Machine Learning Exercise 0: Dataset Description

A reproducible dataset-exploration project for the TU Wien Machine Learning course (Winter Semester 2026). The exercise compares two classification datasets: **Credit Card Fraud Classification** and **Adult ASD Screening**. It documents dataset structure, feature types and measurement scales, missing values, class distributions, numeric ranges, and selected data-quality observations.

> **Academic context:** This repository documents a course exercise. Follow the instructor’s guidance on collaboration, AI assistance, citation, and what may be shared publicly. The GitHub repository does not replace the official TUWEL submission.

## At a glance

| Dataset | Rows | Attributes | Target | Key observation |
|---|---:|---:|---|---|
| Credit Card Fraud Classification | 28,480 | 31 | `class` | Strong class imbalance: 49 fraud cases (about 0.17%) |
| Adult ASD Screening | 704 | 21 | `Class/ASD` | 192 missing cells in the original attributes; one age value of 383 is flagged for review |

These counts describe the versions analysed for this exercise. The scripts print the statistics again from the local source files.

## Repository contents

```text
 tu-wien-ml-exercise-0/
 ├── data/
 │   └── README.md                 # where to place the two local ARFF files
 ├── plots/
 │   ├── dataset_distributions.png # targets, transaction amount, age
 │   └── categorical_distributions.png # ASD gender and ethnicity
 ├── report/
 │   ├── Exercise0_Report.pdf      # two-page report
 │   └── Exercise0_Report_Source.docx # editable report source
 ├── scripts/
 │   ├── inspect_datasets.py       # structure, types, missing values, summaries
 │   ├── feature_analysis.py       # detailed feature/target and quality checks
 │   └── plot_distributions.py     # reproducible figures
 ├── .gitignore
 ├── requirements.txt
 └── README.md
```

## 1. What the project does

1. Loads the two ARFF datasets into pandas DataFrames.
2. Converts ARFF `?` markers into missing values for analysis.
3. Reports the number of records and attributes, column names, data types, missing values, numeric summaries, and target-class counts/percentages.
4. Examines numeric ranges and highlights the ASD age value `383` as a possible data-quality issue. It is **flagged, not silently corrected or deleted**.
5. Creates figures showing target distributions, transaction amounts, age distribution, gender distribution, and ethnicity distribution.
6. Supports the written report with reproducible analysis scripts and saved figures.

## 2. Set up the project

### Requirements

- Python 3.10 or newer (the project was prepared in a Python 3.12 workflow).
- pip.
- The two original ARFF dataset files, obtained from the sources specified by the course materials.

### Windows — VS Code / PowerShell

Open this repository folder in VS Code. In the VS Code terminal, run:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, use Command Prompt and run:

```bat
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Add the datasets

The raw datasets are not included in this GitHub repository. This avoids redistributing files without confirming their licence and keeps the repository lightweight.

1. Obtain both datasets using the source links or instructions in the official TU Wien assignment materials.
2. Put them in the `data/` folder.
3. Use these exact base filenames:
   - `Credit_Card_Fraud_Classification`
   - `Autism-Screening`
4. The current scripts expect these names without an extension. If your files end in `.arff`, rename them to the exact names above, or update the corresponding filenames in the scripts.
5. Keep the original values unchanged. The scripts handle `?` as missing data during loading.

See [`data/README.md`](data/README.md) for the same instructions.

## 4. Run the analysis

Run commands from the repository root, in this order:

```bash
python scripts/inspect_datasets.py
python scripts/feature_analysis.py
python scripts/plot_distributions.py
```

The scripts print their findings in the terminal. The plotting script saves:

- `plots/dataset_distributions.png`
- `plots/categorical_distributions.png`

The feature-analysis script saves `plots/missing_values_report.csv`. CSV outputs are ignored by Git by default; remove that ignore rule if you intentionally want to version the generated CSV.

## 5. What to look for in the results

### Credit Card Fraud Classification

- 28,480 records and 31 attributes in the analysed copy.
- Target distribution: 28,431 `otherwise` and 49 `fraud` cases (approximately 99.83% and 0.17%).
- Transaction `amount` is non-negative in the analysed data and strongly right-skewed; the report gives the descriptive statistics.
- The target is nominal. The transaction amount is a ratio-scale measurement. The transformed `v1`–`v28` features are numeric, but their original semantic units are not available from the feature names alone.

### Adult ASD Screening

- 704 records and 21 attributes in the analysed copy.
- Target distribution: 515 `NO` and 189 `YES` (approximately 73.15% and 26.85%).
- Original missing cells: 2 in `age`, 95 in `ethnicity`, and 95 in `relation` (192 in total).
- The recorded maximum age is 383. This is treated as a data-quality flag, not automatically changed.
- `A1_Score`–`A10_Score` are binary 0/1 fields; `result` is a 0–10 score. Confirm any derived-feature relationship against the data before using it as a predictor, because it may cause target leakage depending on the prediction task.

## 6. Measurement scales and preprocessing considerations

The report discusses nominal, ordinal, interval, and ratio scales. Do not assign a measurement scale based only on a column's numeric storage type. For example, encoded categories are not automatically continuous measurements. Potential preprocessing considerations include missing-value handling, encoding nominal features, scaling numeric features where the chosen model requires it, and examining outliers. Any fitted preprocessing must be learned from training data only when building predictive models.

## 7. Reproducibility and troubleshooting

- Run commands from the repository root so the relative project paths resolve correctly.
- Check that the two files are inside `data/` and their names match the expected names exactly.
- If `ModuleNotFoundError` appears, activate the virtual environment and run `python -m pip install -r requirements.txt` again.
- If an ARFF parsing error occurs, confirm that the file is the original ARFF version and was not opened and re-saved in a way that changed its format.
- The scripts do not repair suspicious values or impute missing values. They report them for review.
- The figures already in `plots/` are the outputs used when preparing the report; rerunning scripts regenerates them from your local data.

## 8. Report and academic integrity

The `report/` folder contains the PDF report and its editable DOCX source. Review the group details, contribution statements, dataset attribution, and course formatting requirements before sharing or submitting. Do not claim that this repository implements a predictive model: this exercise is focused on dataset description and exploratory analysis.

## 9. Suggested citation / attribution

Cite the original dataset providers and the TU Wien course assignment according to the instructions in the course materials. The precise provider citation/licence should be copied from the dataset source page or assignment handout; it is intentionally not guessed here.

## 10. Contact / project ownership

Prepared as a student course project by the listed group members in the report. For questions about the scripts or reproducibility, open a GitHub Issue or contact the repository maintainer through their GitHub profile.
