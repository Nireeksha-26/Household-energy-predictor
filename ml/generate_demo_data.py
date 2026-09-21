import numpy as np
import pandas as pd
from pathlib import Path


# -----------------------------
# Configuration
# -----------------------------

RANDOM_SEED = 42
NUMBER_OF_RECORDS = 4000

np.random.seed(RANDOM_SEED)


# -----------------------------
# Generate input features
# -----------------------------

data = pd.DataFrame({
    "temperature": np.random.uniform(18, 38, NUMBER_OF_RECORDS),

    "humidity": np.random.uniform(30, 90, NUMBER_OF_RECORDS),

    "occupants": np.random.randint(
        1, 7, NUMBER_OF_RECORDS
    ),

    "ac_hours": np.random.uniform(
        0, 10, NUMBER_OF_RECORDS
    ),

    "refrigerator_hours": np.random.uniform(
        18, 24, NUMBER_OF_RECORDS
    ),

    "washing_machine_hours": np.random.uniform(
        0, 4, NUMBER_OF_RECORDS
    ),

    "tv_hours": np.random.uniform(
        0, 10, NUMBER_OF_RECORDS
    ),

    "lighting_hours": np.random.uniform(
        0, 12, NUMBER_OF_RECORDS
    ),

    "computer_hours": np.random.uniform(
        0, 10, NUMBER_OF_RECORDS
    ),

    "other_appliance_hours": np.random.uniform(
        0, 6, NUMBER_OF_RECORDS
    ),

    "previous_consumption": np.random.uniform(
        2, 15, NUMBER_OF_RECORDS
    ),

    "hour": np.random.randint(
        0, 24, NUMBER_OF_RECORDS
    ),

    "day_of_week": np.random.randint(
        0, 7, NUMBER_OF_RECORDS
    ),

    "month": np.random.randint(
        1, 13, NUMBER_OF_RECORDS
    )
})


# -----------------------------
# Generate target
# -----------------------------

data["energy_consumption"] = (
    0.25 * data["occupants"]
    + 0.8 * data["ac_hours"]
    + 0.15 * data["refrigerator_hours"]
    + 0.5 * data["washing_machine_hours"]
    + 0.35 * data["tv_hours"]
    + 0.25 * data["lighting_hours"]
    + 0.3 * data["computer_hours"]
    + 0.2 * data["other_appliance_hours"]
    + 0.3 * data["previous_consumption"]
    + 0.03 * data["temperature"]
    + np.random.normal(0, 0.5, NUMBER_OF_RECORDS)
)


# Prevent negative consumption values
data["energy_consumption"] = data[
    "energy_consumption"
].clip(lower=0.1)


# -----------------------------
# Save CSV
# -----------------------------

project_root = Path(__file__).resolve().parent.parent

data_directory = project_root / "data"

data_directory.mkdir(
    parents=True,
    exist_ok=True
)

output_file = data_directory / "energy_data.csv"

data.to_csv(
    output_file,
    index=False
)


# -----------------------------
# Display result
# -----------------------------

print("Dataset created successfully!")
print(f"Records: {len(data)}")
print(f"Columns: {len(data.columns)}")
print(f"Saved to: {output_file}")

print("\nFirst 5 rows:")
print(data.head())

print("\nMissing values:")
print(data.isnull().sum())

print("\nDataset shape:")
print(data.shape)