def smart_budget_insight(df_expense, total_income):

    if total_income == 0 or df_expense.empty:
        return ["Not enough data"]

    insights = []

    # Category grouping
    needs = ['Rent', 'Food', 'Utilities']
    wants = ['Entertainment', 'Shopping', 'Travel']

    total_expense = df_expense['amount'].sum()

    # Actual spending
    needs_spend = df_expense[df_expense['category'].isin(needs)]['amount'].sum()
    wants_spend = df_expense[df_expense['category'].isin(wants)]['amount'].sum()

    # Ideal spending
    ideal_needs = total_income * 0.5
    ideal_wants = total_income * 0.3

    # Compare needs
    if needs_spend > ideal_needs:
        diff = needs_spend - ideal_needs
        insights.append(f"⚠ Needs spending is high by ₹{round(diff,2)}")
    else:
        insights.append("✅ Needs spending is under control")

    # Compare wants
    if wants_spend > ideal_wants:
        diff = wants_spend - ideal_wants
        insights.append(f"⚠ Wants spending is high by ₹{round(diff,2)}")
    else:
        insights.append("✅ Wants spending is balanced")

    # Savings insight
    savings = total_income - total_expense
    ideal_savings = total_income * 0.2

    if savings < ideal_savings:
        insights.append("⚠ Your savings are below recommended 20%")
    else:
        insights.append("✅ Good savings habit")

    return insights