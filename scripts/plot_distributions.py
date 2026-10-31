
from pathlib import Path

import arff
import pandas as pd
import matplotlib.pyplot as plt

# Set the paths relative to this script
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
PLOTS_DIR = PROJECT_DIR / "plots"

PLOTS_DIR.mkdir(parents=True, exist_ok=True)


def load_dataset(file_name):
    """Load an ARFF dataset into a pandas DataFrame."""
    file_path = DATA_DIR / file_name

    with open(file_path, "r", encoding="utf-8-sig") as file:
        dataset = arff.load(file)

    df = pd.DataFrame(
        dataset["data"],
        columns=[attribute[0] for attribute in dataset["attributes"]]
    )

    # Treat the ARFF '?' marker as a missing value
    df = df.replace("?", pd.NA)

    return df


# Read the two datasets
fraud_df = load_dataset("Credit_Card_Fraud_Classification")
asd_df = load_dataset("Autism-Screening")

# Convert the fields used in the plots to numbers
fraud_df["amount"] = pd.to_numeric(
    fraud_df["amount"], errors="coerce"
)

asd_df["age_numeric"] = pd.to_numeric(
    asd_df["age"], errors="coerce"
)

# Put the four plots together in one figure
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Plot the fraud and non-fraud counts
fraud_counts = fraud_df["class"].value_counts()

axes[0, 0].bar(
    fraud_counts.index.astype(str),
    fraud_counts.values
)
axes[0, 0].set_title("Credit Card Fraud: Target Distribution")
axes[0, 0].set_xlabel("Transaction Class")
axes[0, 0].set_ylabel("Number of Transactions")

# Show the distribution of transaction amounts
axes[0, 1].hist(
    fraud_df["amount"].dropna(),
    bins=40,
    edgecolor="black"
)
axes[0, 1].set_title("Credit Card Fraud: Transaction Amounts")
axes[0, 1].set_xlabel("Transaction Amount")
axes[0, 1].set_ylabel("Frequency")

# Plot the ASD class counts
asd_counts = asd_df["Class/ASD"].value_counts()

axes[1, 0].bar(
    asd_counts.index.astype(str),
    asd_counts.values
)
axes[1, 0].set_title("ASD Screening: Target Distribution")
axes[1, 0].set_xlabel("ASD Classification")
axes[1, 0].set_ylabel("Number of Individuals")

# Show the distribution of ages
axes[1, 1].hist(
    asd_df["age_numeric"].dropna(),
    bins=20,
    edgecolor="black"
)
axes[1, 1].set_title("ASD Screening: Age Distribution")
axes[1, 1].set_xlabel("Age")
axes[1, 1].set_ylabel("Frequency")

plt.tight_layout()

output_file = PLOTS_DIR / "dataset_distributions.png"
plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.show()

print(f"Graphs saved to: {output_file}")
print(f"Fraud dataset rows: {len(fraud_df)}")
print(f"ASD dataset rows: {len(asd_df)}")
print(f"Age values that could not be converted: {asd_df['age_numeric'].isna().sum()}")


# ---------------------------------------------------------
# Figure 2: Categorical distributions in the ASD dataset
# ---------------------------------------------------------

# Work on a copy so the original data stays unchanged
asd_categorical = asd_df.copy()

# Remove surrounding quote characters from category labels
# Check the cleaned labels against the source data before submitting
for column in ["gender", "ethnicity"]:
    asd_categorical[column] = asd_categorical[column].apply(
        lambda value: (
            value.strip().strip("'\"").strip()
            if isinstance(value, str) and value.strip() != "?"
            else value
        )
    )

# Show missing values as their own category
gender_counts = (
    asd_categorical["gender"]
    .fillna("Missing")
    .value_counts()
)

ethnicity_counts = (
    asd_categorical["ethnicity"]
    .fillna("Missing")
    .value_counts()
)

# Put the gender and ethnicity charts side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Gender counts
axes[0].bar(
    gender_counts.index.astype(str),
    gender_counts.values,
    edgecolor="black"
)
axes[0].set_title("ASD Screening: Gender Distribution")
axes[0].set_xlabel("Gender")
axes[0].set_ylabel("Number of Individuals")
axes[0].tick_params(axis="x", rotation=30)

# Ethnicity counts
axes[1].bar(
    ethnicity_counts.index.astype(str),
    ethnicity_counts.values,
    edgecolor="black"
)
axes[1].set_title("ASD Screening: Ethnicity Distribution")
axes[1].set_xlabel("Ethnicity")
axes[1].set_ylabel("Number of Individuals")
axes[1].tick_params(axis="x", rotation=60)

plt.tight_layout()

# Save the figure in the plots folder
categorical_output = PLOTS_DIR / "categorical_distributions.png"
plt.savefig(categorical_output, dpi=300, bbox_inches="tight")

print(f"Categorical graphs saved to: {categorical_output}")
print("\nGender counts (including missing values):")
print(gender_counts)
print("\nEthnicity counts (including missing values):")
print(ethnicity_counts)

plt.show()

