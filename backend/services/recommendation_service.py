def generate_recommendations(input_data, predicted_consumption):

    recommendations = []

    # High overall consumption
    if predicted_consumption >= 20:
        recommendations.append(
            "Your predicted energy consumption is high. "
            "Try reducing unnecessary appliance usage."
        )

    elif predicted_consumption >= 12:
        recommendations.append(
            "Your predicted energy consumption is moderate. "
            "Monitor high-usage appliances to reduce consumption."
        )

    else:
        recommendations.append(
            "Your predicted energy consumption is low. "
            "Continue using appliances efficiently."
        )

    # Air conditioner
    if input_data["ac_hours"] > 6:
        recommendations.append(
            "AC usage is high. Consider reducing AC operating hours "
            "and using a reasonable temperature setting."
        )

    # Refrigerator
    if input_data["refrigerator_hours"] > 24:
        recommendations.append(
            "Check refrigerator usage and ensure the door is not "
            "being opened unnecessarily."
        )

    # Washing machine
    if input_data["washing_machine_hours"] > 2:
        recommendations.append(
            "Try running the washing machine with full loads "
            "when appropriate."
        )

    # Television
    if input_data["tv_hours"] > 6:
        recommendations.append(
            "Consider reducing TV usage when it is not needed."
        )

    # Lighting
    if input_data["lighting_hours"] > 8:
        recommendations.append(
            "Switch off lights when rooms are unoccupied "
            "and use efficient lighting where possible."
        )

    # Computer
    if input_data["computer_hours"] > 6:
        recommendations.append(
            "Turn off or put the computer into sleep mode "
            "when it is not being used."
        )

    # Other appliances
    if input_data["other_appliance_hours"] > 4:
        recommendations.append(
            "Reduce unnecessary usage of other electrical appliances."
        )

    return recommendations