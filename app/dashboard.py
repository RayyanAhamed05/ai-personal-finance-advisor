import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


from src.anomaly_detection import detect_anomalies
from src.budget_advisor import recommend_budget
from src.subscription_detector import detect_subscriptions
from src.financial_health import calculate_financial_health
from src.smart_budget import smart_budget_insight
from src.emi_calculator import calculate_emi
from src.project_chatbot import project_chatbot
from src.forecasting import forecast_expenses
from src.risk_predictor import predict_financial_risk
from src.what_if_analysis import run_what_if_analysis
from src.goal_savings_planner import goal_based_savings_planner

st.set_page_config(page_title="AI Finance Advisor", layout="wide")
st.markdown("""
<style>

/* =========================
   MAIN PAGE SPACING
========================= */

.block-container {
    padding-top: 3rem;
    padding-bottom: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* =========================
   METRICS
========================= */

[data-testid="stMetricValue"] {
    font-size: 26px;
    font-weight: 600;
}

[data-testid="stMetricLabel"] {
    font-size: 14px;
}

/* =========================
   HEADINGS
========================= */

h1 {
    font-size: 2rem !important;
}

h2 {
    font-size: 1.5rem !important;
}

h3 {
    font-size: 1.1rem !important;
}

/* =========================
   GENERAL TEXT
========================= */

p, li {
    font-size: 15px;
}

/* =========================
   BUTTONS
========================= */

.stButton > button {
    padding: 0.45rem 1rem;
    border-radius: 10px;
    font-size: 14px;
}

/* =========================
   ALERT / INFO BOXES
========================= */

div[data-baseweb="notification"] {
    padding: 10px;
    border-radius: 10px;
}

/* =========================
   DATAFRAME
========================= */

[data-testid="stDataFrame"] {
    font-size: 13px;
}

/* =========================
   TABS
========================= */

button[data-baseweb="tab"] {
    font-size: 16px;
    padding: 10px 18px;
}

/* =========================
   SLIDER
========================= */

.stSlider {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* =========================
   PROGRESS BAR
========================= */

.stProgress > div > div > div {
    height: 12px;
}

/* =========================
   INPUT BOXES
========================= */

.stTextInput input,
.stNumberInput input {
    font-size: 14px;
}

/* =========================
   SELECTBOX
========================= */

.stSelectbox div[data-baseweb="select"] {
    font-size: 14px;
}

/* =========================
   IMAGE ROUNDING
========================= */

img {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)
df = pd.DataFrame()


# =========================
# SIDEBAR INPUT
# =========================
st.sidebar.header("📥 Data Input")

option = st.sidebar.radio("Input Method", ["Upload CSV", "Manual Entry"])

df = pd.DataFrame()

if option == "Upload CSV":
    file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if file:
        df = pd.read_csv(file)

elif option == "Manual Entry":
    if "data" not in st.session_state:
        st.session_state.data = []

    date = st.sidebar.date_input("Date")
    category = st.sidebar.selectbox("Category",
        ["Food","Rent","Travel","Shopping","Utilities","Entertainment"])
    amount = float(st.sidebar.number_input("Amount", min_value=0.0))
    desc = st.sidebar.text_input("Description")
    ttype = st.sidebar.selectbox("Type", ["Expense","Income"])

    if st.sidebar.button("Add Entry"):
        st.session_state.data.append({
            "date": str(date),
            "category": category,
            "amount": amount,
            "description": desc,
            "type": ttype
        })

    if st.session_state.data:
        df = pd.DataFrame(st.session_state.data)

if df.empty:
        # =========================
    # LANDING PAGE
    # =========================

    st.title("💡 Transforming Personal Finance with AI Solutions")

    st.markdown("""
    ### Intelligent Financial Decision Support System

    This AI-powered platform helps users analyze expenses,
    predict future spending, detect anomalies, evaluate
    financial health, simulate scenarios, and receive
    smart financial recommendations.
    """)

    st.image(
        "https://images.unsplash.com/photo-1559526324-593bc073d938",
        width=850
    )

    st.markdown("---")

    # ROW 1
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
    📈 Expense Forecasting

    Predict future expenses using AI-powered
    time-series forecasting models.
    """)

    with col2:
        st.info("""
    ⚠ Anomaly Detection

    Detect unusual spending patterns and
    financial risks automatically.
    """)

    with col3:
        st.info("""
    💰 Smart Budgeting

    Generate intelligent savings and
    budgeting recommendations.
    """)

    # ROW 2
    col4, col5, col6 = st.columns(3)

    with col4:
        st.info("""
    🏦 EMI Planning

    Analyze loan feasibility and
    EMI impact on savings.
    """)

    with col5:
        st.info("""
    🤖 AI Financial Assistant

    Interact with a context-aware
    finance chatbot assistant.
    """)

    with col6:
        st.info("""
    🔄 What-if Analysis

    Simulate financial scenarios and
    evaluate decision impact.
    """)

    # ROW 3
    col7, col8, col9 = st.columns(3)

    with col7:
        st.info("""
    ❤️ Financial Health Score

    Evaluate financial stability using
    AI-driven financial metrics.
    """)

    with col8:
        st.info("""
    📊 Investment Advisor

    Get smart Mutual Fund and FD
    allocation recommendations.
    """)

    with col9:
        st.info("""
    ⚡ AI Risk Predictor

    Predict financial risks using
    intelligent AI analysis.
    """)

    # ROW 4
    col10, col11, col12 = st.columns(3)

    with col10:
        st.info("""
    📺 Subscription Detection

    Detect recurring subscriptions
    and hidden monthly expenses.
    """)

    with col11:
        st.info("""
    📉 Expense Visualization

    Analyze financial data using
    interactive charts and trends.
    """)

    with col12:
        st.info("""
    🧠 AI Decision Support

    Transform raw financial data into
    actionable intelligent insights.
    """)

    st.markdown("---")

    st.markdown("""
    ## Project Overview

    This platform integrates Machine Learning,
    Predictive Analytics, Financial Forecasting,
    Risk Detection, and Conversational AI into a
    unified personal finance advisory system.

    The application converts raw financial
    transactions into intelligent insights that
    help users improve budgeting, forecasting,
    risk management, and financial decision-making.
    """)

# =========================
# MAIN LOGIC
# =========================
if not df.empty:

    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # =========================
    # SIDEBAR FILTERS
    # =========================
    st.sidebar.header("🔍 Filters")

    start, end = st.sidebar.date_input(
        "Date Range",
        [df['date'].min(), df['date'].max()]
    )

    selected_cat = st.sidebar.multiselect(
        "Category",
        df['category'].unique(),
        default=df['category'].unique()
    )

    df = df[
        (df['date'] >= pd.to_datetime(start)) &
        (df['date'] <= pd.to_datetime(end)) &
        (df['category'].isin(selected_cat))
    ]

    df_exp = df[df['type']=="Expense"]
    df_inc = df[df['type']=="Income"]

    total_exp = df_exp['amount'].sum()
    total_inc = df_inc['amount'].sum()
    savings = total_inc - total_exp

    # =========================
    # TABS
    # =========================
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Dashboard",
        "📈 AI Insights",
        "🏦 Financial Planning",
        "🤖 Assistant"
    ])

    # =========================
    # DASHBOARD
    # =========================
    with tab1:

        col1,col2,col3 = st.columns(3)
        col1.metric("Income", total_inc)
        col2.metric("Expense", total_exp)
        col3.metric("Savings", savings)

        st.dataframe(df)

        if not df_exp.empty:
            cat = df_exp.groupby('category')['amount'].sum()

            col1,col2 = st.columns(2)

            with col1:
                fig, ax = plt.subplots(figsize=(5,4))
                cat.plot(kind='bar', ax=ax)
                plt.tight_layout()
                st.pyplot(fig)

            with col2:
                fig2, ax2 = plt.subplots(figsize=(5,4))

                def autopct(p):
                    return f"{p:.1f}%" if p > 5 else ""

                cat.plot(kind='pie', ax=ax2, autopct=autopct)
                ax2.set_ylabel("")
                st.pyplot(fig2)

                # =========================
        # IMPROVED MONTHLY TREND
        # =========================

        df_exp_copy = df_exp.copy()

        # Create month column safely
        df_exp_copy['month'] = df_exp_copy['date'].dt.to_period('M').dt.to_timestamp()

        # Group by month
        monthly = df_exp_copy.groupby('month')['amount'].sum().reset_index()

        # Sort properly
        monthly = monthly.sort_values('month')

        # Remove invalid/zero months
        monthly = monthly[monthly['amount'] > 0]

        if not monthly.empty:

            fig, ax = plt.subplots(figsize=(8,4))

            ax.plot(monthly['month'], monthly['amount'], marker='o')

            ax.set_title("Monthly Expense Trend")
            ax.set_xlabel("Month")
            ax.set_ylabel("Amount")

            # 🔥 Highlight anomalies
            threshold = monthly['amount'].mean() * 1.5

            added_label = False

            for i in range(len(monthly)):
                if monthly.iloc[i]['amount'] > threshold:
                    ax.scatter(
                        monthly.iloc[i]['month'],
                        monthly.iloc[i]['amount'],
                        color='red',
                        s=100,
                        label='High Expense' if not added_label else ""
                    )
                    added_label = True

            ax.grid(True)
            ax.legend()
            plt.tight_layout()
            st.pyplot(fig)
    # =========================
    # AI INSIGHTS
    # =========================
    with tab2:

        st.subheader("⚠ Anomaly Detection")

        anomalies = pd.DataFrame()

        if len(df_exp) > 5:
            anomalies = detect_anomalies(df_exp)
            st.write(anomalies if not anomalies.empty else "No anomalies")

        st.subheader("📺 Subscription Detection")

        if "description" in df.columns:

            subs = detect_subscriptions(df_exp)

            if not subs.empty:
                st.dataframe(subs)

        # 🔥 Extra Insight (Good for marks)
                total_sub_cost = subs['amount'].sum()
                st.write(f"Total Monthly Subscription Cost: ₹{round(total_sub_cost,2)}")

            else:
                st.success("No subscriptions detected")

        # =========================
# FINANCIAL HEALTH SCORE
# =========================

        st.subheader("📊 Financial Health Analysis")

        score, label = calculate_financial_health(
            total_inc,
            total_exp,
            len(anomalies)
        )

        # -------------------------
        # TOP METRICS
        # -------------------------

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Health Score",
                f"{score:.1f}/100"
            )

        with c2:

            savings_ratio = (
                (savings / total_inc) * 100
                if total_inc > 0 else 0
            )

            st.metric(
                "Savings Ratio",
                f"{savings_ratio:.1f}%"
            )

        with c3:
            st.metric(
                "Anomalies",
                len(anomalies)
            )

        st.divider()

        # -------------------------
        # HEALTH STATUS
        # -------------------------

        st.markdown("### ❤️ Financial Status")

        if score >= 75:

            st.success(
                "Excellent Financial Health"
            )

        elif score >= 50:

            st.warning(
                "Moderate Financial Health"
            )

        else:

            st.error(
                "Poor Financial Health"
            )

        # -------------------------
        # HEALTH PROGRESS
        # -------------------------

        st.markdown("### 📈 Financial Stability")

        progress_value = int(score)

        st.progress(progress_value)

        st.caption(
            f"Overall Financial Stability: {score:.1f}%"
        )

        st.divider()

        # -------------------------
        # AI RECOMMENDATIONS
        # -------------------------

        st.markdown("### 🧠 AI Recommendations")

        recommendations = []

        if savings_ratio < 20:
            recommendations.append(
                "Increase monthly savings ratio."
            )

        if len(anomalies) > 3:
            recommendations.append(
                "Monitor unusual spending patterns."
            )

        if total_exp > total_inc:
            recommendations.append(
                "Expenses exceed income."
            )

        if not recommendations:
            recommendations.append(
                "Your financial behavior appears stable."
            )

        for rec in recommendations:
            st.info(rec)
        
        st.subheader("🧠 Smart Insights")
        insights = smart_budget_insight(
        df_exp,
        total_inc
        )
        for i in insights:

            st.success(f" {i}")
        
        # =========================
# FORECASTING
# =========================

        st.subheader("📈 Expense Forecasting")

        if len(df_exp) > 5:

            model, forecast = forecast_expenses(df_exp)

            fig1 = model.plot(forecast)
            fig1.set_size_inches(9, 4)
            plt.tight_layout()
            st.pyplot(fig1)

            st.write(
                forecast[['ds', 'yhat']].tail(3)
            )

        # -------------------------
# ADVANCED WHAT-IF ANALYSIS
# -------------------------

        st.subheader("🔄 AI What-if Analysis")

        if not df_exp.empty:

            # =========================
            # INPUTS
            # =========================

            c1, c2 = st.columns(2)

            with c1:

                cat_sel = st.selectbox(
                    "Select Expense Category",
                    df_exp['category'].unique()
                )

            with c2:

                change = st.slider(
                    "Expense Change (%)",
                    min_value=-50,
                    max_value=50,
                    value=-10
                )

            # =========================
            # RUN BUTTON
            # =========================

            if st.button("Run AI Simulation"):

                # Run Analysis
                result = run_what_if_analysis(
                    df_exp,
                    total_inc,
                    cat_sel,
                    change
                )

                # =========================
                # SIMULATION RESULTS
                # =========================

                st.markdown("### 📊 Simulation Results")

                # TOP METRICS
                m1, m2, m3 = st.columns(3)

                with m1:
                    st.metric(
                        "Old Expense",
                        f"₹{result['old_expense']:,.0f}"
                    )

                with m2:
                    st.metric(
                        "New Expense",
                        f"₹{result['new_expense']:,.0f}"
                    )

                with m3:
                    st.metric(
                        "Difference",
                        f"₹{result['difference']:,.0f}"
                    )

                # SECOND ROW
                m4, m5, m6, m7 = st.columns(4)

                with m4:
                    st.metric(
                        "Old Savings",
                        f"₹{result['old_savings']:,.0f}"
                    )

                with m5:
                    st.metric(
                        "New Savings",
                        f"₹{result['new_savings']:,.0f}"
                    )

                with m6:
                    st.metric(
                        "Savings Ratio",
                        f"{result['new_ratio']}%"
                    )

                with m7:
                    st.metric(
                        "Health Score",
                        f"{result['health_score']}/100"
                    )

                st.divider()

                # =========================
                # RISK + RECOMMENDATION
                # =========================

                left, right = st.columns([1,2])

                # RISK
                with left:

                    st.markdown("### ⚠ Risk Status")

                    if result['risk'] == "Low Risk":

                        st.success("Low Risk")

                    elif result['risk'] == "Moderate Risk":

                        st.warning("Moderate Risk")

                    else:

                        st.error("High Risk")

                # AI RECOMMENDATION
                with right:

                    st.markdown("### 🧠 AI Recommendation")

                    st.info(result['advice'])
    # =========================
    # FINANCIAL PLANNING
    # =========================
    with tab3:

           # =========================
# SMART BUDGET ADVISOR
# =========================

        st.subheader("💰 Smart Budget Advisor")

        monthly_income = st.number_input(
            "Monthly Income",
            value=30000
        )

        budget = recommend_budget(monthly_income)

        # =========================
        # TOP METRICS
        # =========================

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric(
                "Savings",
                f"₹{budget['Savings']:,.0f}"
            )

        with m2:
            essential_total = (
                budget['Rent']
                + budget['Food']
                + budget['Utilities']
            )

            st.metric(
                "Essential",
                f"₹{essential_total:,.0f}"
            )

        with m3:
            st.metric(
                "Other",
                f"₹{budget['Other']:,.0f}"
            )

        st.divider()

        # =========================
        # CHART + INSIGHTS
        # =========================

        left, right = st.columns([1,1])

        # -------------------------
        # PIE CHART
        # -------------------------

        with left:

            st.markdown("### 📊 Distribution")

            budget_df = pd.DataFrame({
                "Category": budget.keys(),
                "Amount": budget.values()
            })

            fig, ax = plt.subplots(figsize=(4,4))

            ax.pie(
                budget_df["Amount"],
                labels=budget_df["Category"],
                autopct='%1.1f%%',
                textprops={'fontsize': 9}
            )

            plt.tight_layout()

            st.pyplot(fig)

        # -------------------------
        # AI INSIGHTS
        # -------------------------

        with right:

            st.markdown("### 🧠 AI Insights")

            savings_ratio = (
                budget['Savings'] / monthly_income
            )

            if savings_ratio >= 0.3:

                st.success(
                    "Healthy savings structure detected."
                )

            elif savings_ratio >= 0.15:

                st.warning(
                    "Moderate savings ratio."
                )

            else:

                st.error(
                    "Low savings ratio detected."
                )

            st.markdown("""
            #### Smart Suggestions

            • Reduce discretionary spending  
            • Maintain emergency savings  
            • Follow 50-30-20 budgeting  
            • Track recurring expenses
            """)

        st.divider()

        # =========================
        # CATEGORY BREAKDOWN
        # =========================

        st.markdown("### 📌 Recommended Allocation")

        for category, amount in budget.items():

            percent = int(
                (amount / monthly_income) * 100
            )

            c1, c2 = st.columns([3,1])

            with c1:

                st.write(
                    f"**{category}**"
                )

                st.progress(percent)

            with c2:

                st.write(
                    f"₹{amount:,.0f}"
                )

                st.caption(
                    f"{percent}%"
                )
                            

        # EMI
        st.subheader("🏦 EMI Planner")

        loan = st.number_input("Loan Amount", value=100000)
        rate = st.number_input("Interest Rate", value=10.0)
        years = st.number_input("Years", value=2)

        emi = calculate_emi(loan, rate, years)
        st.metric("EMI", f"₹{round(emi,2)}")

        months = df['date'].dt.to_period('M').nunique()
        monthly_exp = total_exp / months if months else 0

        savings_before = monthly_income - monthly_exp
        savings_after = savings_before - emi

        st.write("Savings After EMI:", round(savings_after,2))

        if savings_after < 0:
            st.error("High Risk Loan")
        elif savings_after < savings_before * 0.2:
            st.warning("Moderate Risk Loan")
        else:
            st.success("Safe Loan")


        # EMI Planner

        # -------------------------
        # FINANCIAL RISK PREDICTOR
        # -------------------------

        st.subheader("⚠ AI Financial Risk Predictor")

        monthly_income = total_inc
        monthly_expense = total_exp

        # Savings
        savings_calc = monthly_income - monthly_expense

        # Expense Growth
        expense_growth = 15

        # Anomaly Count
        anomaly_count = len(anomalies)

        risk, score = predict_financial_risk(
            monthly_income,
            monthly_expense,
            savings_calc,
            emi,
            anomaly_count,
            expense_growth
        )

        st.metric("Risk Score", score)

        if risk == "Low Risk":
            st.success(f"Risk Level: {risk}")

        elif risk == "Moderate Risk":
            st.warning(f"Risk Level: {risk}")

        else:
            st.error(f"Risk Level: {risk}")



        # Investment
        st.subheader("📊 Investment")

        age = st.number_input("Age", 18, 60, 25)
        risk = st.selectbox("Risk", ["Low","Medium","High"])

        savings_calc = monthly_income - monthly_exp

        equity = 100 - age
        if risk == "Low": equity -= 20
        elif risk == "High": equity += 15

        equity = max(20,min(equity,80))
        debt = 100 - equity

        mf = savings_calc * equity/100
        fd = savings_calc * debt/100

        if savings_calc > 0:
            st.write("MF:", mf)
            st.write("FD:", fd)

        
        # -------------------------
# GOAL-BASED SAVINGS PLANNER
# -------------------------

        st.subheader("🎯 Goal-Based Smart Savings Planner")

        goal_name = st.text_input(
            "Financial Goal",
            placeholder="Example: Car, House, Education"
        )

        target_amount = st.number_input(
            "Target Amount (₹)",
            min_value=1000.0,
            value=500000.0
        )

        duration = st.number_input(
            "Goal Duration (Months)",
            min_value=1,
            value=24
        )

        current_monthly_savings = st.number_input(
            "Current Monthly Savings (₹)",
            min_value=0.0,
            value=float(max(savings, 0))
        )

        if st.button("Analyze Goal"):

            result = goal_based_savings_planner(
                goal_name,
                target_amount,
                duration,
                current_monthly_savings
            )

            st.markdown("## 📊 Goal Analysis")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Required Monthly Savings",
                    f"₹{result['required_monthly']:,.0f}"
                )

            with c2:
                st.metric(
                    "Current Savings",
                    f"₹{result['current_savings']:,.0f}"
                )

            with c3:
                st.metric(
                    "Savings Gap",
                    f"₹{result['gap']:,.0f}"
                )

            st.divider()

            st.markdown("## 📈 Goal Feasibility")

            st.progress(
                int(result['completion_percent'])
            )

            st.write(
                f"Goal Readiness: {result['completion_percent']}%"
            )

            # Status
            if result['risk'] == "Low":
                st.success(f"Status: {result['status']}")

            elif result['risk'] == "Moderate":
                st.warning(f"Status: {result['status']}")

            else:
                st.error(f"Status: {result['status']}")

            st.markdown("## 🧠 AI Recommendation")

            st.info(result['suggestion'])

    # =========================
    # CHATBOT
    # =========================
    with tab4:

# -------------------------
# AI CHATBOT
# -------------------------

        st.subheader("🤖 AI Finance Assistant")

        st.markdown("### 💬 Suggested Questions")

        # Suggested Prompt Buttons
        c1, c2 = st.columns(2)

        with c1:

            if st.button("📊 Analyze my expenses"):
                st.session_state.chat_input = "Analyze my expenses"

            if st.button("💰 How are my savings?"):
                st.session_state.chat_input = "How are my savings"

            if st.button("🏦 Can I afford a loan?"):
                st.session_state.chat_input = "Can I afford a loan"

            if st.button("⚠ Show financial risk"):
                st.session_state.chat_input = "Show financial risk"

        with c2:

            if st.button("📈 Give investment advice"):
                st.session_state.chat_input = "Give investment advice"

            if st.button("❤️ Check financial health"):
                st.session_state.chat_input = "Check financial health"

            if st.button("📺 Detect subscriptions"):
                st.session_state.chat_input = "Detect subscriptions"

            if st.button("🔄 Explain what-if analysis"):
                st.session_state.chat_input = "Explain what-if analysis"

        # Initialize session state
        if "chat_input" not in st.session_state:
            st.session_state.chat_input = ""

        # Text Input
        msg = st.text_input(
            "Ask your finance question",
            value=st.session_state.chat_input
        )

        # Send Button
        if st.button("Send", key="chat_send"):

            if msg:

                res = project_chatbot(
                    msg,
                    df_exp,
                    total_inc,
                    total_exp,
                    savings,
                    anomalies
                )

                st.success(res)

                # Clear after response
                st.session_state.chat_input = ""