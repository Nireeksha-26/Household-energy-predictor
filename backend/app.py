from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from backend.models.database_models import db

from backend.routes.prediction_routes import prediction_bp
from backend.routes.auth_routes import auth_bp
from backend.routes.history_routes import history_bp
from backend.routes.dashboard_routes import dashboard_bp


# =========================================================
# CREATE FLASK APPLICATION
# =========================================================

app = Flask(__name__)


# =========================================================
# CORS CONFIGURATION
# =========================================================

CORS(app)


# =========================================================
# DATABASE CONFIGURATION
# =========================================================

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///energy.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# =========================================================
# JWT CONFIGURATION
# =========================================================

# Temporary secret key for development.
# Later we will move this into a .env file.
app.config["JWT_SECRET_KEY"] = "change-this-secret-key-later"


# =========================================================
# INITIALIZE DATABASE
# =========================================================

db.init_app(app)


# =========================================================
# INITIALIZE JWT
# =========================================================

jwt = JWTManager(app)


# =========================================================
# REGISTER BLUEPRINTS
# =========================================================

# Prediction routes
app.register_blueprint(
    prediction_bp
)

# Authentication routes
app.register_blueprint(
    auth_bp
)

# History routes
app.register_blueprint(
    history_bp
)

# Dashboard routes
app.register_blueprint(
    dashboard_bp
)


# =========================================================
# HOME ROUTE
# =========================================================

@app.route("/")
def home():

    return {
        "message": "Household Energy Prediction API is running!"
    }


# =========================================================
# HEALTH CHECK ROUTE
# =========================================================

@app.route("/api/health")
def health():

    return {

        "status": "OK",

        "message": "Backend is healthy"

    }


# =========================================================
# CREATE DATABASE TABLES
# =========================================================

with app.app_context():

    db.create_all()


# =========================================================
# RUN FLASK APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )