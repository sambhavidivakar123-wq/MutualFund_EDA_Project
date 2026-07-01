import pandas as pd
import os

# Folder containing raw CSV files
data_folder = "data/raw"

# Get all CSV files
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

print("=" * 60)
print(f"Found {len(csv_files)} CSV file(s)")
print("=" * 60)

for file in csv_files:
    file_path = os.path.join(data_folder, file)

    print(f"\n📄 File: {file}")

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n" + "=" * 60)