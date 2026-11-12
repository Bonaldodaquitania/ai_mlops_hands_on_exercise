from pathlib import Path
from zipfile import ZipFile
import pandas as pd

# Locate the dataset in the project root
project_root = Path(__file__).resolve().parents[2]
dataset_path = project_root / "datasets" / "bike_sharing.zip"

# Load hourly observations from the ZIP archive
with ZipFile(dataset_path) as archive:
    with archive.open("hour.csv") as file:
        df = pd.read_csv(file)

# Inspect dataset structure
print("Dataset dimensions:")
print(df.shape)

print("\nFirst five rows:")
print(df.head())

print("\nDataset information:")
df.info()



# Descriptive statistics for the target
print("\nTarget descriptive statistics:")
print(df["cnt"].describe())

# Descriptive statistics for weather-related features
print("\nWeather features statistics:")
print(df[["temp", "atemp", "hum", "windspeed"]].describe())



# Check missing values for each column
print("\nMissing values:")
print(df.isna().sum())

# Check duplicated date-hour observations
print("\nDuplicate observations:")
print(df.duplicated(subset=["dteday", "hr"]).sum())

# Check consistency between target and user categories
print("\nInconsistent rental counts:")
print((df["casual"] + df["registered"] != df["cnt"]).sum())



# Detect potential OUTLINERS in hourly rental counts using IQR
q1 = df["cnt"].quantile(0.25)
q3 = df["cnt"].quantile(0.75)

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[
    (df["cnt"] < lower_bound) |
    (df["cnt"] > upper_bound)
]

print("\nOutlier detection (IQR method):")
print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Lower bound: {lower_bound}")
print(f"Upper bound: {upper_bound}")
print(f"Potential outliers: {len(outliers)}")

