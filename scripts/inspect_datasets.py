
from pathlib import Path

import pandas as pd
import arff

# Set the project and data folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Dataset filenames used in this project
dataset_files = {
    "Credit Card Fraud": "Credit_Card_Fraud_Classification",
    "Adult ASD Screening": "Autism-Screening",
}


def load_dataset(file_path):
    """Load an ARFF dataset using liac-arff."""
    with open(file_path, "r", encoding="utf-8-sig") as file:
        dataset = arff.load(file)

    df = pd.DataFrame(
        dataset["data"],
        columns=[attribute[0] for attribute in dataset["attributes"]]
    )

    # Convert ARFF missing-value markers to pandas missing values
    df = df.replace("?", pd.NA)

    return df


for dataset_name, filename_start in dataset_files.items():

    # Find the file whether or not it has an extension
    matches = [
        p for p in DATA_DIR.iterdir()
        if p.is_file() and (
            p.name == filename_start
            or p.name.startswith(filename_start + ".")
        )
    ]

    print("\n" + "=" * 60)
    print(dataset_name)
    print("=" * 60)

    if len(matches) != 1:
        print("Expected one matching file, found:", len(matches))
        print("Check the filename in the data folder.")
        continue

    file_path = matches[0]
    print("File:", file_path.name)

    try:
        df = load_dataset(file_path)
    except Exception as error:
        print("Could not load this file as ARFF.")
        print("Error:", error)
        continue

    # Show the number of rows and columns
    print("\nDimensions (rows, columns):", df.shape)

    # List the columns and their data types
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    # Count missing values in each column
    print("\nMissing values per column:")
    print(df.isna().sum())

    # Summarize numeric columns
    print("\nNumerical summary:")
    print(df.describe().T)

    # Summarize categorical columns
    print("\nCategorical summary:")
    print(df.describe(include=["object"]).T)

    # Check the class counts and percentages
    target_candidates = {
        "Credit Card Fraud": ["class"],
        "Adult ASD Screening": ["Class/ASD", "Class_ASD"],
    }

    target = next(
        (column for column in target_candidates[dataset_name]
         if column in df.columns),
        None,
    )

    if target is not None:
        print("\nTarget distribution:")
        print(df[target].value_counts(dropna=False))

        print("\nTarget percentages:")
        print(
            (df[target].value_counts(normalize=True, dropna=False) * 100)
            .round(2)
        )
    else:
        print("\nTarget column not found. Check the printed column names.")
