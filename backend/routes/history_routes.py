from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.models.database_models import EnergyRecord


history_bp = Blueprint(
    "history",
    __name__
)


# =========================================================
# GET USER HISTORY
# =========================================================

@history_bp.route(
    "/api/history",
    methods=["GET"]
)
@jwt_required()
def get_history():

    try:

        # Get logged-in user's ID from JWT
        user_id = get_jwt_identity()

        # Get only records belonging to this user
        records = EnergyRecord.query.filter_by(
            user_id=int(user_id)
        ).order_by(
            EnergyRecord.created_at.desc()
        ).all()

        history = []

        for record in records:

            history.append({

                "id": record.id,

                "date": record.date.isoformat(),

                "temperature": record.temperature,

                "humidity": record.humidity,

                "occupants": record.occupants,

                "ac_hours": record.ac_hours,

                "refrigerator_hours": record.refrigerator_hours,

                "washing_machine_hours": record.washing_machine_hours,

                "tv_hours": record.tv_hours,

                "lighting_hours": record.lighting_hours,

                "computer_hours": record.computer_hours,

                "other_appliance_hours": record.other_appliance_hours,

                "previous_consumption": record.previous_consumption,

                "hour": record.hour,

                "day_of_week": record.day_of_week,

                "month": record.month,

                "actual_consumption": record.actual_consumption,

                "predicted_consumption": record.predicted_consumption,

                "created_at": record.created_at.isoformat()

            })

        return jsonify({

            "history": history

        }), 200

    except Exception:

        return jsonify({

            "error": "Unable to fetch history."

        }), 500


# =========================================================
# DELETE USER HISTORY RECORD
# =========================================================

@history_bp.route(
    "/api/history/<int:record_id>",
    methods=["DELETE"]
)
@jwt_required()
def delete_history(record_id):

    try:

        from backend.models.database_models import db

        # Get logged-in user's ID
        user_id = get_jwt_identity()

        # Find record belonging to this user
        record = EnergyRecord.query.filter_by(
            id=record_id,
            user_id=int(user_id)
        ).first()

        if not record:

            return jsonify({

                "error": "History record not found."

            }), 404

        db.session.delete(record)

        db.session.commit()

        return jsonify({

            "message": "History record deleted successfully."

        }), 200

    except Exception:

        return jsonify({

            "error": "Unable to delete history record."

        }), 500