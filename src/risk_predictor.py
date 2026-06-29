def predict_financial_risk(
    income,
    expenses,
    savings,
    emi,
    anomaly_count,
    expense_growth
):

    risk_score = 0

    # -------------------------
    # Savings Ratio
    # -------------------------
    if income > 0:
        savings_ratio = savings / income
    else:
        savings_ratio = 0

    if savings_ratio < 0.1:
        risk_score += 3

    elif savings_ratio < 0.2:
        risk_score += 2

    else:
        risk_score += 1

    # -------------------------
    # EMI Burden
    # -------------------------
    if income > 0:
        emi_ratio = emi / income
    else:
        emi_ratio = 0

    if emi_ratio > 0.5:
        risk_score += 3

    elif emi_ratio > 0.3:
        risk_score += 2

    else:
        risk_score += 1

    # -------------------------
    # Expense Trend
    # -------------------------
    if expense_growth > 20:
        risk_score += 3

    elif expense_growth > 10:
        risk_score += 2

    else:
        risk_score += 1

    # -------------------------
    # Anomaly Frequency
    # -------------------------
    if anomaly_count > 10:
        risk_score += 3

    elif anomaly_count > 5:
        risk_score += 2

    else:
        risk_score += 1

    # -------------------------
    # Final Risk Classification
    # -------------------------
    if risk_score <= 4:
        risk = "Low Risk"

    elif risk_score <= 8:
        risk = "Moderate Risk"

    else:
        risk = "High Risk"

    return risk, risk_score