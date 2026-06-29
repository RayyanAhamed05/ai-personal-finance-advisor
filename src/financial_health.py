def calculate_financial_health(total_income, total_expense, anomalies_count):

    if total_income == 0:
        return 0, "No Income Data"

    # Savings ratio score (40)
    savings = total_income - total_expense
    savings_ratio = savings / total_income

    savings_score = max(0, min(40, savings_ratio * 40))

    # Expense stability (30)
    if total_expense == 0:
        stability_score = 30
    else:
        stability_score = 30 - (anomalies_count * 5)
        stability_score = max(0, stability_score)

    # Anomaly score (30)
    anomaly_score = max(0, 30 - anomalies_count * 5)

    total_score = savings_score + stability_score + anomaly_score

    # Label
    if total_score >= 75:
        label = "Excellent"
    elif total_score >= 60:
        label = "Good"
    elif total_score >= 40:
        label = "Average"
    else:
        label = "Poor"

    return round(total_score, 2), label