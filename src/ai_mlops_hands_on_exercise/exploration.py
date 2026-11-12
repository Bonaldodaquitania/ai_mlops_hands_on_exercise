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
