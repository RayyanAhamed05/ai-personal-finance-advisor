import pandas as pd


def run_what_if_analysis(
    df_exp,
    total_income,
    category,
    change_percent
):

    sim = df_exp.copy()

    sim['amount'] = sim['amount'].astype(float)

    # Original Expense
    original_expense = sim['amount'].sum()

    # Apply simulation
    sim.loc[
        sim['category'] == category,
        'amount'
    ] *= (1 + change_percent / 100)

    # New Expense
    new_expense = sim['amount'].sum()

    # Savings
    old_savings = total_income - original_expense
    new_savings = total_income - new_expense

    # Savings Ratio
    old_ratio = (
        old_savings / total_income * 100
        if total_income > 0 else 0
    )

    new_ratio = (
        new_savings / total_income * 100
        if total_income > 0 else 0
    )

    # Financial Health Score
    health_score = max(
        0,
        min(
            100,
            int(
                new_ratio * 1.5
            )
        )
    )

    # Risk Classification
    if new_ratio >= 40:
        risk = "Low Risk"

    elif new_ratio >= 20:
        risk = "Moderate Risk"

    else:
        risk = "High Risk"

    # Essential Categories
    essential = [
        "Rent",
        "Food",
        "Utilities"
    ]

    # AI Recommendation
    if category in essential and change_percent < 0:

        advice = (
            f"Reducing {category} expenses may affect "
            f"essential living standards."
        )

    elif change_percent < 0:

        advice = (
            f"Reducing {category} spending improves "
            f"your savings and financial stability."
        )

    else:

        advice = (
            f"Increasing {category} expenses may "
            f"reduce long-term savings."
        )

    # Expense Difference
    diff = new_expense - original_expense

    return {
        "old_expense": round(original_expense, 2),
        "new_expense": round(new_expense, 2),
        "old_savings": round(old_savings, 2),
        "new_savings": round(new_savings, 2),
        "difference": round(diff, 2),
        "old_ratio": round(old_ratio, 2),
        "new_ratio": round(new_ratio, 2),
        "health_score": health_score,
        "risk": risk,
        "advice": advice
    }