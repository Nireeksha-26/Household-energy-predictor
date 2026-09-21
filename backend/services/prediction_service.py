import joblib
import pandas as pd

from pathlib import Path


# ---------------------------------
# Project paths
# ---------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

MODEL_FILE = (
    PROJECT_ROOT
    / "models"
    / "energy_model.pkl"
)

PIPELINE_FILE = (
    PROJECT_ROOT
    / "models"
    / "preprocessing_pipeline.pkl"
)


# ---------------------------------
# Feature order
# ---------------------------------

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


# ---------------------------------
# Load model and pipeline
# ---------------------------------

model = joblib.load(MODEL_FILE)

preprocessing_pipeline = joblib.load(
    PIPELINE_FILE
)


# ---------------------------------
# Prediction function
# ---------------------------------

def predict_energy(input_data):

    # Create DataFrame
    input_df = pd.DataFrame(
        [input_data],
        columns=FEATURES
    )

    # Apply preprocessing
    processed_data = (
        preprocessing_pipeline.transform(
            input_df
        )
    )

    # Generate prediction
    prediction = model.predict(
        processed_data
    )[0]

    # Prevent negative prediction
    prediction = max(
        0,
        float(prediction)
    )

    return round(
        prediction,
        2
    )