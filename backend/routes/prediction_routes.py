from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date

from backend.models.database_models import db, EnergyRecord
from backend.services.prediction_service import predict_energy
from backend.services.recommendation_service import generate_recommendations
from backend.utils.validation import validate_input


prediction_bp = Blueprint(
    "prediction",
    __name__
)


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


# =========================================================
# PREDICT ENERGY CONSUMPTION
# =========================================================

@prediction_bp.route(
    "/api/predict",
    methods=["POST"]
)
@jwt_required()
def predict():

    try:

        # Get logged-in user's ID
        user_id = get_jwt_identity()

        # Get request data
        data = request.get_json()

        if not data:

            return jsonify({
                "error": "Request body is required."
            }), 400

        # Validate input
        validation_errors = validate_input(data)

        if validation_errors:

            return jsonify({

                "error": "Invalid input.",

                "details": validation_errors

            }), 400

        # Make prediction
        prediction = predict_energy(data)

        # Determine consumption category
        if prediction < 12:

            category = "Low"

        elif prediction < 20:

            category = "Moderate"

        else:

            category = "High"

        # Generate recommendations
        recommendations = generate_recommendations(
            data,
            prediction
        )

        # =================================================
        # SAVE PREDICTION TO DATABASE
        # =================================================

        new_record = EnergyRecord(

            user_id=int(user_id),

            date=date.today(),

            temperature=data["temperature"],

            humidity=data["humidity"],

            occupants=data["occupants"],

            ac_hours=data["ac_hours"],

            refrigerator_hours=data["refrigerator_hours"],

            washing_machine_hours=data["washing_machine_hours"],

            tv_hours=data["tv_hours"],

            lighting_hours=data["lighting_hours"],

            computer_hours=data["computer_hours"],

            other_appliance_hours=data["other_appliance_hours"],

            previous_consumption=data["previous_consumption"],

            hour=data["hour"],

            day_of_week=data["day_of_week"],

            month=data["month"],

            actual_consumption=None,

            predicted_consumption=prediction

        )

        db.session.add(new_record)

        db.session.commit()

        # =================================================
        # RESPONSE
        # =================================================

        return jsonify({

            "message": "Prediction successful.",

            "record_id": new_record.id,

            "predicted_energy_consumption": prediction,

            "unit": "kWh",

            "category": category,

            "recommendations": recommendations

        }), 200

    except Exception as error:

        db.session.rollback()

        return jsonify({

            "error": "Prediction failed.",

            "details": str(error)

        }), 500