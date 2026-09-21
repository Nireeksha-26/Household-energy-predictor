import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from xgboost import XGBRegressor


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

DATA_FILE = (
    PROJECT_ROOT
    / "data"
    / "energy_data.csv"
)

PIPELINE_FILE = (
    PROJECT_ROOT
    / "models"
    / "preprocessing_pipeline.pkl"
)

MODEL_DIRECTORY = PROJECT_ROOT / "models"

MODEL_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True
)


# ---------------------------------
# Load dataset
# ---------------------------------

print("Loading dataset...")

data = pd.read_csv(DATA_FILE)

print(
    f"Dataset shape: {data.shape}"
)


# ---------------------------------
# Prepare features and target
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

print(
    f"Training samples: {len(X_train)}"
)

print(
    f"Testing samples: {len(X_test)}"
)


# ---------------------------------
# Load preprocessing pipeline
# ---------------------------------

print("\nLoading preprocessing pipeline...")

preprocessing_pipeline = joblib.load(
    PIPELINE_FILE
)

print("Pipeline loaded successfully.")


# ---------------------------------
# Transform data
# ---------------------------------

X_train_processed = (
    preprocessing_pipeline.transform(X_train)
)

X_test_processed = (
    preprocessing_pipeline.transform(X_test)
)


# ---------------------------------
# Random Forest
# ---------------------------------

print("\nTraining Random Forest...")

random_forest = RandomForestRegressor(
    n_estimators=200,
    random_state=RANDOM_SEED,
    n_jobs=-1
)

random_forest.fit(
    X_train_processed,
    y_train
)

rf_predictions = random_forest.predict(
    X_test_processed
)


# ---------------------------------
# XGBoost
# ---------------------------------

print("\nTraining XGBoost...")

xgboost_model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=6,
    random_state=RANDOM_SEED,
    objective="reg:squarederror",
    n_jobs=-1
)

xgboost_model.fit(
    X_train_processed,
    y_train
)

xgb_predictions = xgboost_model.predict(
    X_test_processed
)


# ---------------------------------
# Evaluation function
# ---------------------------------

def evaluate_model(
    model_name,
    actual,
    predictions
):

    mae = mean_absolute_error(
        actual,
        predictions
    )

    mse = mean_squared_error(
        actual,
        predictions
    )

    rmse = mse ** 0.5

    r2 = r2_score(
        actual,
        predictions
    )

    print(f"\n{model_name}")
    print("----------------------------")
    print(f"MAE  : {mae:.4f}")
    print(f"MSE  : {mse:.4f}")
    print(f"RMSE : {rmse:.4f}")
    print(f"R²   : {r2:.4f}")

    return {
        "model": model_name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2
    }


# ---------------------------------
# Evaluate models
# ---------------------------------

rf_results = evaluate_model(
    "Random Forest",
    y_test,
    rf_predictions
)

xgb_results = evaluate_model(
    "XGBoost",
    y_test,
    xgb_predictions
)


# ---------------------------------
# Compare models
# ---------------------------------

results = pd.DataFrame([
    rf_results,
    xgb_results
])

print("\nModel Comparison")
print("================")
print(results.to_string(index=False))


# ---------------------------------
# Select final model
# ---------------------------------

# Primary criterion: lowest RMSE
# Tie-breaker: highest R²

if (
    rf_results["RMSE"] < xgb_results["RMSE"]
):

    final_model = random_forest
    final_model_name = "Random Forest"

else:

    final_model = xgboost_model
    final_model_name = "XGBoost"


# ---------------------------------
# Save final model
# ---------------------------------

MODEL_FILE = (
    MODEL_DIRECTORY
    / "energy_model.pkl"
)

joblib.dump(
    final_model,
    MODEL_FILE
)


# ---------------------------------
# Save evaluation results
# ---------------------------------

RESULTS_FILE = (
    MODEL_DIRECTORY
    / "model_results.csv"
)

results.to_csv(
    RESULTS_FILE,
    index=False
)


# ---------------------------------
# Final output
# ---------------------------------

print("\nFinal Model")
print("================")
print(
    f"Selected model: {final_model_name}"
)

print(
    f"Model saved to: {MODEL_FILE}"
)

print(
    f"Results saved to: {RESULTS_FILE}"
)

print(
    "\nModel training completed successfully!"
)