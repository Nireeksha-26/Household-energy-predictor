from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import func

from backend.models.database_models import EnergyRecord


dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


# =========================================================
# DASHBOARD
# =========================================================

@dashboard_bp.route(
    "/api/dashboard",
    methods=["GET"]
)
@jwt_required()
def dashboard():

    try:

        # Get logged-in user's ID
        user_id = get_jwt_identity()

        user_id = int(user_id)

        # Get all records for this user
        records = EnergyRecord.query.filter_by(
            user_id=user_id
        ).order_by(
            EnergyRecord.created_at.desc()
        ).all()

        # -------------------------------------------------
        # No records
        # -------------------------------------------------

        if not records:

            return jsonify({

                "total_predictions": 0,

                "average_consumption": 0,

                "latest_prediction": None,

                "highest_consumption": 0,

                "lowest_consumption": 0,

                "energy_status": "No data",

                "recent_records": []

            }), 200

        # -------------------------------------------------
        # Consumption values
        # -------------------------------------------------

        consumption_values = [
            record.predicted_consumption
            for record in records
        ]

        total_predictions = len(
            consumption_values
        )

        average_consumption = (
            sum(consumption_values)
            / total_predictions
        )

        highest_consumption = max(
            consumption_values
        )

        lowest_consumption = min(
            consumption_values
        )

        latest_record = records[0]

        # -------------------------------------------------
        # Energy status
        # -------------------------------------------------

        if average_consumption < 12:

            energy_status = "Low"

        elif average_consumption < 20:

            energy_status = "Moderate"

        else:

            energy_status = "High"

        # -------------------------------------------------
        # Recent records
        # -------------------------------------------------

        recent_records = []

        for record in records[:10]:

            recent_records.append({

                "id": record.id,

                "date": record.date.isoformat(),

                "predicted_consumption":
                    record.predicted_consumption,

                "actual_consumption":
                    record.actual_consumption

            })

        # -------------------------------------------------
        # Response
        # -------------------------------------------------

        return jsonify({

            "total_predictions":
                total_predictions,

            "average_consumption":
                round(average_consumption, 2),

            "latest_prediction": {

                "id": latest_record.id,

                "date":
                    latest_record.date.isoformat(),

                "predicted_consumption":
                    latest_record.predicted_consumption,

                "category":
                    (
                        "Low"
                        if latest_record.predicted_consumption < 12
                        else
                        "Moderate"
                        if latest_record.predicted_consumption < 20
                        else
                        "High"
                    )

            },

            "highest_consumption":
                round(highest_consumption, 2),

            "lowest_consumption":
                round(lowest_consumption, 2),

            "energy_status":
                energy_status,

            "recent_records":
                recent_records

        }), 200

    except Exception:

        return jsonify({

            "error": "Unable to load dashboard data."

        }), 500