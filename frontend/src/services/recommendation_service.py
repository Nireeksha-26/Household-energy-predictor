def generate_recommendations(input_data, predicted_consumption):

    recommendations = []

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

    if input_data["ac_hours"] > 6:
        recommendations.append(
            "AC usage is high. Consider reducing AC operating hours "
            "and using a reasonable temperature setting."
        )

    if input_data["washing_machine_hours"] > 2:
        recommendations.append(
            "Try running the washing machine with full loads "
            "when appropriate."
        )

    if input_data["tv_hours"] > 6:
        recommendations.append(
            "Consider reducing TV usage when it is not needed."
        )

    if input_data["lighting_hours"] > 8:
        recommendations.append(
            "Switch off lights when rooms are unoccupied "
            "and use efficient lighting where possible."
        )

    if input_data["computer_hours"] > 6:
        recommendations.append(
            "Turn off or put the computer into sleep mode "
            "when it is not being used."
        )

    if input_data["other_appliance_hours"] > 4:
        recommendations.append(
            "Reduce unnecessary usage of other electrical appliances."
        )

    return recommendations