import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


# ---------------------------------
# Configuration
# ---------------------------------

RANDOM_SEED = 42
TEST_SIZE = 0.20

FEATURES = [
    "temperature",
    "humidity",
    "occupants",
    "ac_hours",
    "refrigerator_hours",
    "washing_machine_hours",
    "tv_hours",
    "lighting_hours",
    "computer_hours",
    "other_appliance_hours",
    "previous_consumption",
    "hour",
    "day_of_week",
    "month"
]

TARGET = "energy_consumption"


# ---------------------------------
# Project paths
# ---------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_ROOT / "data" / "energy_data.csv"

MODELS_DIRECTORY = PROJECT_ROOT / "models"

MODELS_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True
)

PIPELINE_FILE = MODELS_DIRECTORY / "preprocessing_pipeline.pkl"


# ---------------------------------
# Load dataset
# ---------------------------------

data = pd.read_csv(DATA_FILE)

print("Dataset loaded successfully!")
print("Original shape:", data.shape)


# ---------------------------------
# Validate columns
# ---------------------------------

required_columns = FEATURES + [TARGET]

missing_columns = [
    column
    for column in required_columns
    if column not in data.columns
]

if missing_columns:
    raise ValueError(
        f"Missing columns: {missing_columns}"
    )

print("\nAll required columns are present.")


# ---------------------------------
# Check missing values
# ---------------------------------

print("\nMissing values:")
print(data[required_columns].isnull().sum())


# ---------------------------------
# Remove duplicate rows
# ---------------------------------

duplicate_count = data.duplicated().sum()

print("\nDuplicate rows:", duplicate_count)

if duplicate_count > 0:
    data = data.drop_duplicates()

print("Shape after removing duplicates:", data.shape)


# ---------------------------------
# Remove invalid target values
# ---------------------------------

invalid_target_count = (
    data[TARGET] <= 0
).sum()

print(
    "\nInvalid target values:",
    invalid_target_count
)

if invalid_target_count > 0:
    data = data[data[TARGET] > 0]


# ---------------------------------
# Separate features and target
# ---------------------------------

X = data[FEATURES]

y = data[TARGET]


# ---------------------------------
# Train-test split
# ---------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_SEED
)


# ---------------------------------
# Create preprocessing pipeline
# ---------------------------------

preprocessing_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median")
        ),
        (
            "scaler",
            StandardScaler()
        )
    ]
)


# ---------------------------------
# Fit ONLY on training data
# ---------------------------------

X_train_processed = preprocessing_pipeline.fit_transform(
    X_train
)

X_test_processed = preprocessing_pipeline.transform(
    X_test
)


# ---------------------------------
# Save preprocessing pipeline
# ---------------------------------

joblib.dump(
    preprocessing_pipeline,
    PIPELINE_FILE
)


# ---------------------------------
# Display results
# ---------------------------------

print("\nTrain/Test Split")
print("----------------")

print(
    "Training samples:",
    len(X_train)
)

print(
    "Testing samples:",
    len(X_test)
)

print(
    "\nProcessed training shape:",
    X_train_processed.shape
)

print(
    "Processed testing shape:",
    X_test_processed.shape
)

print(
    "\nPreprocessing pipeline saved to:"
)

print(PIPELINE_FILE)

print(
    "\nPreprocessing completed successfully!"
)