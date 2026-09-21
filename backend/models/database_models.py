from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    energy_records = db.relationship(
        "EnergyRecord",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )


class EnergyRecord(db.Model):

    __tablename__ = "energy_records"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    date = db.Column(
        db.Date,
        nullable=False
    )

    temperature = db.Column(
        db.Float,
        nullable=False
    )

    humidity = db.Column(
        db.Float,
        nullable=False
    )

    occupants = db.Column(
        db.Integer,
        nullable=False
    )

    ac_hours = db.Column(
        db.Float,
        nullable=False
    )

    refrigerator_hours = db.Column(
        db.Float,
        nullable=False
    )

    washing_machine_hours = db.Column(
        db.Float,
        nullable=False
    )

    tv_hours = db.Column(
        db.Float,
        nullable=False
    )

    lighting_hours = db.Column(
        db.Float,
        nullable=False
    )

    computer_hours = db.Column(
        db.Float,
        nullable=False
    )

    other_appliance_hours = db.Column(
        db.Float,
        nullable=False
    )

    previous_consumption = db.Column(
        db.Float,
        nullable=False
    )

    hour = db.Column(
        db.Integer,
        nullable=False
    )

    day_of_week = db.Column(
        db.Integer,
        nullable=False
    )

    month = db.Column(
        db.Integer,
        nullable=False
    )

    actual_consumption = db.Column(
        db.Float,
        nullable=True
    )

    predicted_consumption = db.Column(
        db.Float,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )