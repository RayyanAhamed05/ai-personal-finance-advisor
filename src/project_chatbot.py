def project_chatbot(
    user_input,
    df_exp,
    total_income,
    total_expense,
    savings,
    anomalies
):

    user_input = user_input.lower()

    # =========================
    # BASIC CALCULATIONS
    # =========================

    savings_ratio = (
        savings / total_income
        if total_income > 0 else 0
    )

    top_category = None

    if not df_exp.empty:
        top_category = (
            df_exp.groupby('category')['amount']
            .sum()
            .idxmax()
        )

    # =========================
    # GREETING
    # =========================

    greetings = [
        "hello", "hi", "hey", "good morning",
        "good evening"
    ]

    if any(word in user_input for word in greetings):

        return (
            "Hello 👋 I am your AI Finance Assistant.\n\n"
            "You can ask me about:\n"
            "- expenses\n"
            "- savings\n"
            "- investments\n"
            "- EMI planning\n"
            "- anomalies\n"
            "- budgeting\n"
            "- financial health\n"
            "- subscriptions\n"
            "- forecasting\n"
            "- risk analysis\n"
            "- goal planning"
        )

    # =========================
    # FINANCIAL HEALTH
    # =========================

    elif any(word in user_input for word in [
        "health",
        "financial health",
        "score"
    ]):

        if total_income == 0:
            return "No income data available."

        if savings_ratio >= 0.4:

            return (
                "✅ Your financial health is excellent.\n\n"
                "You maintain a strong savings ratio "
                "and healthy spending behavior."
            )

        elif savings_ratio >= 0.2:

            return (
                "⚠ Your financial health is moderate.\n\n"
                "Try reducing unnecessary spending "
                "to improve savings."
            )

        else:

            return (
                "❌ Your financial health is poor.\n\n"
                "Your expenses are consuming most "
                "of your income."
            )

    # =========================
    # EXPENSE ANALYSIS
    # =========================

    elif any(word in user_input for word in [
        "expense",
        "spending",
        "highest spending"
    ]):

        if top_category:

            return (
                f"📊 Your highest spending category is "
                f"'{top_category}'.\n\n"
                f"Consider optimizing this category "
                f"to improve savings."
            )

        return "No expense data available."

    # =========================
    # SAVINGS
    # =========================

    elif any(word in user_input for word in [
        "saving",
        "savings"
    ]):

        if savings <= 0:

            return (
                "⚠ You are currently not saving money.\n\n"
                "Reduce non-essential expenses and "
                "improve budgeting discipline."
            )

        return (
            f"💰 Your current savings are "
            f"₹{round(savings,2)}.\n\n"
            f"Your savings ratio is "
            f"{round(savings_ratio*100,2)}%."
        )

    # =========================
    # EMI / LOAN
    # =========================

    elif any(word in user_input for word in [
        "emi",
        "loan",
        "debt"
    ]):

        if savings_ratio < 0.1:

            return (
                "❌ Taking a loan may be risky.\n\n"
                "Your current savings are very low."
            )

        elif savings_ratio < 0.25:

            return (
                "⚠ EMI should be planned carefully.\n\n"
                "Maintain an emergency fund before "
                "taking large loans."
            )

        else:

            return (
                "✅ Your financial position appears "
                "stable enough for manageable EMI planning."
            )

    # =========================
    # INVESTMENT
    # =========================

    elif any(word in user_input for word in [
        "invest",
        "investment",
        "mutual fund",
        "fd",
        "sip"
    ]):

        if savings <= 0:

            return (
                "⚠ You currently do not have sufficient "
                "savings for investments."
            )

        elif savings < 5000:

            return (
                "📈 Start with low-risk SIPs or "
                "Fixed Deposits for stable growth."
            )

        else:

            return (
                "📊 You may diversify investments into:\n\n"
                "- Mutual Funds\n"
                "- SIPs\n"
                "- Fixed Deposits\n"
                "- Emergency Funds"
            )

    # =========================
    # ANOMALIES
    # =========================

    elif any(word in user_input for word in [
        "anomaly",
        "unusual",
        "fraud",
        "suspicious"
    ]):

        if len(anomalies) == 0:

            return (
                "✅ No unusual financial transactions "
                "were detected."
            )

        return (
            f"⚠ {len(anomalies)} unusual transactions "
            f"were detected.\n\n"
            f"Please review your spending carefully."
        )

    # =========================
    # SUBSCRIPTIONS
    # =========================

    elif any(word in user_input for word in [
        "subscription",
        "netflix",
        "spotify",
        "recurring"
    ]):

        subs = df_exp[df_exp['amount'] < 1000]

        if subs.empty:

            return (
                "✅ No recurring subscriptions detected."
            )

        return (
            "📺 Small recurring payments detected.\n\n"
            "Review entertainment and app subscriptions "
            "to optimize expenses."
        )

    # =========================
    # BUDGETING
    # =========================

    elif any(word in user_input for word in [
        "budget",
        "budgeting"
    ]):

        return (
            "💡 Recommended Budget Strategy:\n\n"
            "- 50% Needs\n"
            "- 30% Wants\n"
            "- 20% Savings\n\n"
            "Reducing discretionary spending can "
            "significantly improve financial health."
        )

    # =========================
    # FORECASTING
    # =========================

    elif any(word in user_input for word in [
        "forecast",
        "prediction",
        "future expense"
    ]):

        return (
            "📈 Expense forecasting analyzes historical "
            "transactions to estimate future spending trends."
        )

    # =========================
    # RISK ANALYSIS
    # =========================

    elif any(word in user_input for word in [
        "risk",
        "financial risk"
    ]):

        if savings_ratio >= 0.4:
            return "✅ Financial risk is currently low."

        elif savings_ratio >= 0.2:
            return "⚠ Financial risk is moderate."

        else:
            return "❌ Financial risk is high."

    # =========================
    # GOAL PLANNING
    # =========================

    elif any(word in user_input for word in [
        "goal",
        "target",
        "future plan"
    ]):

        return (
            "🎯 Use the Goal-Based Savings Planner "
            "to analyze your financial goals and "
            "monthly savings requirements."
        )

    # =========================
    # WHAT-IF ANALYSIS
    # =========================

    elif any(word in user_input for word in [
        "what if",
        "simulation",
        "scenario"
    ]):

        return (
            "🔄 The What-if Analysis module helps "
            "simulate expense changes and evaluate "
            "their impact on savings and financial health."
        )

    # =========================
    # DEFAULT RESPONSE
    # =========================

    return (
        "🤖 I can help you with:\n\n"
        "- Expense Analysis\n"
        "- Savings Insights\n"
        "- EMI Planning\n"
        "- Investment Advice\n"
        "- Financial Health\n"
        "- Risk Prediction\n"
        "- Goal Planning\n"
        "- Budgeting\n"
        "- Forecasting\n"
        "- What-if Analysis"
    )