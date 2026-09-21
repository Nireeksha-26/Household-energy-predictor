def validate_input(data):

    errors = []

    required_fields = [
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

    # Check required fields
    for field in required_fields:
        if field not in data:
            errors.append(
                f"{field} is required."
            )

    # Stop if required fields are missing
    if errors:
        return errors

    # Check data types
    for field in required_fields:
        if not isinstance(
            data[field],
            (int, float)
        ):
            errors.append(
                f"{field} must be a number."
            )

    # Stop if data types are incorrect
    if errors:
        return errors

    # Occupants validation
    if data["occupants"] < 0:
        errors.append(
            "Occupants cannot be negative."
        )

    # Appliance hour fields
    appliance_fields = [
        "ac_hours",
        "refrigerator_hours",
        "washing_machine_hours",
        "tv_hours",
        "lighting_hours",
        "computer_hours",
        "other_appliance_hours"
    ]

    # Appliance hours must be between 0 and 24
    for field in appliance_fields:

        if not 0 <= data[field] <= 24:

            errors.append(
                f"{field} must be between 0 and 24 hours."
            )

    # Temperature validation
    if not -20 <= data["temperature"] <= 60:

        errors.append(
            "Temperature must be between -20 and 60°C."
        )

    # Humidity validation
    if not 0 <= data["humidity"] <= 100:

        errors.append(
            "Humidity must be between 0 and 100%."
        )

    # Previous consumption validation
    if data["previous_consumption"] < 0:

        errors.append(
            "Previous consumption cannot be negative."
        )

    # Hour validation
    if not 0 <= data["hour"] <= 23:

        errors.append(
            "Hour must be between 0 and 23."
        )

    # Day of week validation
    if not 0 <= data["day_of_week"] <= 6:

        errors.append(
            "Day of week must be between 0 and 6."
        )

    # Month validation
    if not 1 <= data["month"] <= 12:

        errors.append(
            "Month must be between 1 and 12."
        )

    return errors