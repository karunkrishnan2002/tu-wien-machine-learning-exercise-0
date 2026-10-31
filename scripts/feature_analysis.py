
from pathlib import Path

import arff
import pandas as pd

# Set the data and output folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
REPORT_DIR = PROJECT_DIR / "plots"
REPORT_DIR.mkdir(parents=True, exist_ok=True)


def load_dataset(file_name):
    """Load an ARFF file and convert '?' markers to missing values."""
    file_path = DATA_DIR / file_name

    with open(file_path, "r", encoding="utf-8-sig") as file:
        dataset = arff.load(file)

    df = pd.DataFrame(
        dataset["data"],
        columns=[attribute[0] for attribute in dataset["attributes"]]
    )

    return df.replace("?", pd.NA)


def analyse_dataset(df, name, target_column):
    print("\n" + "=" * 70)
    print(f"DATASET: {name}")
    print("=" * 70)

    # Dataset size
    print("\n1. DATASET DIMENSIONS")
    print(f"Rows (samples): {df.shape[0]}")
    print(f"Columns (attributes): {df.shape[1]}")
    print(f"Input features: {df.shape[1] - 1}")

    # Column data types
    print("\n2. DATA TYPES")
    print(df.dtypes.to_string())

    # Missing-value check
    print("\n3. MISSING VALUES")
    missing = df.isna().sum()
    missing = missing[missing > 0]

    if missing.empty:
        print("No missing values detected.")
    else:
        print(missing.to_string())
        print(f"Total missing cells: {int(missing.sum())}")

    # Summary of numeric columns
    print("\n4. NUMERICAL FEATURE STATISTICS")
    numeric_df = df.select_dtypes(include="number")

    if not numeric_df.empty:
        print(
            numeric_df.describe()
            .round(3)
            .to_string()
        )
    else:
        print("No numerical columns detected.")

    # Counts and percentages for the target
    print("\n5. TARGET DISTRIBUTION")
    print(df[target_column].value_counts(dropna=False).to_string())
    print("\nTarget percentages:")
    print(
        (df[target_column].value_counts(normalize=True, dropna=False) * 100)
        .round(2)
        .to_string()
    )


# Read both datasets
fraud_df = load_dataset("Credit_Card_Fraud_Classification")
asd_df = load_dataset("Autism-Screening")

# Convert fields that should be numeric
fraud_df["time"] = pd.to_numeric(fraud_df["time"], errors="coerce")
fraud_df["amount"] = pd.to_numeric(fraud_df["amount"], errors="coerce")

asd_df["age_numeric"] = pd.to_numeric(asd_df["age"], errors="coerce")

# Print a summary for each dataset
analyse_dataset(
    fraud_df,
    "Credit Card Fraud Classification",
    "class"
)

analyse_dataset(
    asd_df,
    "Adult ASD Screening",
    "Class/ASD"
)

# Check for unusual age values
print("\n" + "=" * 70)
print("ASD AGE QUALITY CHECK")
print("=" * 70)

valid_ages = asd_df["age_numeric"].dropna()

print(f"Missing or non-numeric age values: {asd_df['age_numeric'].isna().sum()}")

if not valid_ages.empty:
    print(f"Minimum age: {valid_ages.min()}")
    print(f"Median age: {valid_ages.median()}")
    print(f"Maximum age: {valid_ages.max()}")

    print("\nLargest five age values:")
    print(valid_ages.nlargest(5).to_string())

    print("\nAge values above 100:")
    print(valid_ages[valid_ages > 100].to_string())

# Save missing-value counts to a CSV file
fraud_missing = fraud_df.isna().sum().rename("Fraud")
asd_missing = asd_df.isna().sum().rename("ASD")

missing_report = pd.concat(
    [fraud_missing, asd_missing],
    axis=1
).fillna(0).astype(int)

output_file = REPORT_DIR / "missing_values_report.csv"
missing_report.to_csv(output_file, index_label="Attribute")

print(f"\nMissing-value report saved to: {output_file}")


# Print the full record for any age above 100
print("\nFULL RECORD WITH AGE 383")
suspicious_record = asd_df[asd_df["age_numeric"] > 100]
print(suspicious_record.T.to_string())

