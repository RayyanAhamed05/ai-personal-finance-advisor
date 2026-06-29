import pandas as pd

def detect_subscriptions(df):

    # Ensure correct format
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = df['amount'].astype(float)

    subscriptions = []

    # 🔹 STEP 1: Keyword-based detection
    keywords = ["netflix", "spotify", "prime", "recharge", "subscription"]

    for i, row in df.iterrows():
        desc = str(row.get("description", "")).lower()

        if any(k in desc for k in keywords):
            subscriptions.append({
                "name": row["description"],
                "amount": row["amount"],
                "type": "Keyword-based"
            })

    # 🔹 STEP 2: Pattern-based detection (IMPORTANT)
    grouped = df.groupby(['description', 'amount'])

    for (desc, amt), group in grouped:

        if len(group) >= 2:

            # Sort by date
            group = group.sort_values('date')

            # Calculate gaps between transactions
            gaps = group['date'].diff().dt.days.dropna()

            # Check if roughly monthly (20–40 days)
            if not gaps.empty and gaps.mean() >= 20 and gaps.mean() <= 40:

                subscriptions.append({
                    "name": desc,
                    "amount": amt,
                    "type": "Recurring (Monthly)"
                })

    # 🔹 Remove duplicates
    result = pd.DataFrame(subscriptions).drop_duplicates()

    return result