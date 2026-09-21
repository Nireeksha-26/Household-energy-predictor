from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from backend.models.database_models import db, User


auth_bp = Blueprint(
    "auth",
    __name__
)


# =========================================================
# REGISTER
# =========================================================

@auth_bp.route(
    "/api/auth/register",
    methods=["POST"]
)
def register():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "error": "Request body is required."
            }), 400

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        # Check required fields
        if not name:

            return jsonify({
                "error": "Name is required."
            }), 400

        if not email:

            return jsonify({
                "error": "Email is required."
            }), 400

        if not password:

            return jsonify({
                "error": "Password is required."
            }), 400

        # Clean input
        name = name.strip()
        email = email.strip().lower()

        # Validate name
        if len(name) < 2:

            return jsonify({
                "error": "Name must contain at least 2 characters."
            }), 400

        # Validate email
        if "@" not in email or "." not in email:

            return jsonify({
                "error": "Please enter a valid email address."
            }), 400

        # Validate password
        if len(password) < 6:

            return jsonify({
                "error": "Password must contain at least 6 characters."
            }), 400

        # Check whether user already exists
        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            return jsonify({
                "error": "An account with this email already exists."
            }), 409

        # Hash password
        password_hash = generate_password_hash(
            password
        )

        # Create user
        new_user = User(
            name=name,
            email=email,
            password_hash=password_hash
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({

            "message": "Registration successful.",

            "user": {
                "id": new_user.id,
                "name": new_user.name,
                "email": new_user.email
            }

        }), 201

    except Exception as error:

        db.session.rollback()

        return jsonify({
            "error": "Registration failed.",
            "details": str(error)
        }), 500


# =========================================================
# LOGIN
# =========================================================

@auth_bp.route(
    "/api/auth/login",
    methods=["POST"]
)
def login():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "error": "Request body is required."
            }), 400

        email = data.get("email")
        password = data.get("password")

        # Check required fields
        if not email:

            return jsonify({
                "error": "Email is required."
            }), 400

        if not password:

            return jsonify({
                "error": "Password is required."
            }), 400

        # Clean email
        email = email.strip().lower()

        # Find user
        user = User.query.filter_by(
            email=email
        ).first()

        if not user:

            return jsonify({
                "error": "Invalid email or password."
            }), 401

        # Check password
        password_valid = check_password_hash(
            user.password_hash,
            password
        )

        if not password_valid:

            return jsonify({
                "error": "Invalid email or password."
            }), 401

        # Create JWT token
        access_token = create_access_token(
            identity=str(user.id)
        )

        return jsonify({

            "message": "Login successful.",

            "access_token": access_token,

            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }

        }), 200

    except Exception as error:

        return jsonify({
            "error": "Login failed.",
            "details": str(error)
        }), 500


# =========================================================
# PROFILE
# =========================================================

@auth_bp.route(
    "/api/profile",
    methods=["GET"]
)
@jwt_required()
def profile():

    try:

        # Get user ID from JWT token
        user_id = get_jwt_identity()

        # Find user in database
        user = User.query.get(
            int(user_id)
        )

        if not user:

            return jsonify({
                "error": "User not found."
            }), 404

        # Return user information
        return jsonify({

            "id": user.id,
            "name": user.name,
            "email": user.email

        }), 200

    except Exception:

        return jsonify({
            "error": "Unable to fetch profile."
        }), 500