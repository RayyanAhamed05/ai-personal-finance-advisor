def goal_based_savings_planner(
    goal_name,
    target_amount,
    duration_months,
    current_savings
):

    # Required monthly savings
    required_monthly = target_amount / duration_months

    # Difference
    gap = required_monthly - current_savings

    # Goal Status
    if current_savings >= required_monthly:

        status = "Achievable"

        suggestion = (
            f"Your current savings pattern is sufficient "
            f"to achieve the {goal_name} goal on time."
        )

        risk = "Low"

    elif current_savings >= required_monthly * 0.7:

        status = "Moderately Achievable"

        suggestion = (
            f"Increase monthly savings slightly or reduce "
            f"non-essential expenses to achieve the "
            f"{goal_name} goal faster."
        )

        risk = "Moderate"

    else:

        status = "Difficult"

        suggestion = (
            f"Your current savings are insufficient for "
            f"the {goal_name} goal. Consider increasing "
            f"income sources, reducing discretionary "
            f"spending, or extending the timeline."
        )

        risk = "High"

    completion_percent = min(
        100,
        round((current_savings / required_monthly) * 100, 2)
    )

    return {
        "goal": goal_name,
        "required_monthly": round(required_monthly, 2),
        "current_savings": round(current_savings, 2),
        "gap": round(gap, 2),
        "status": status,
        "risk": risk,
        "completion_percent": completion_percent,
        "suggestion": suggestion
    }