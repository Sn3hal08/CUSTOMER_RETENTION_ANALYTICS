import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
import pandas as pd
import numpy as np

from src.data_preprocessing import load_data, clean_data
from src.feature_engineering import add_features


BASE_DIR=Path(__file__).resolve().parent.parent
DATA_PATH=BASE_DIR/"data"/"European_Bank.csv"

st.set_page_config(
    page_title="Customer Retention Analytics",
    page_icon="📊",
    layout="wide"
)


# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

@st.cache_data
def load_customer_data():

    df = load_data(DATA_PATH)
    df = clean_data(df)

    return df


df = load_customer_data()


# ---------------------------------------------------------
# FEATURE ENGINEERING
# ---------------------------------------------------------

df = add_features(df)


# ---------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------

def calculate_retention_score(
        credit_score,
        age,
        tenure,
        balance,
        num_products,
        has_card,
        active_member,
        salary
):

    # Normalize credit score
    credit_score_score = min(max((credit_score - 300) / 550, 0), 1)

    # Normalize tenure
    tenure_score = min(tenure / 10, 1)

    # Product score
    product_score = min(num_products / 4, 1)

    # Balance score
    balance_score = min(balance / 200000, 1)

    # Salary score
    salary_score = min(salary / 200000, 1)

    # Activity
    activity_score = active_member

    # Credit card
    card_score = has_card

    # Weighted retention score
    score = (
        credit_score_score * 0.15 +
        tenure_score * 0.15 +
        product_score * 0.20 +
        balance_score * 0.15 +
        salary_score * 0.10 +
        activity_score * 0.20 +
        card_score * 0.05
    )

    return round(score * 100, 2)


def get_risk_level(score):

    if score >= 70:
        return "Low Risk"

    elif score >= 45:
        return "Medium Risk"

    else:
        return "High Risk"


def get_engagement_level(active, products):

    if active == 1 and products >= 2:
        return "Highly Engaged"

    elif active == 1:
        return "Moderately Engaged"

    elif active == 0 and products >= 2:
        return "Disengaged - Multi Product"

    else:
        return "Low Engagement"


def get_recommendation(risk, active, products, balance):

    if risk == "High Risk":

        if active == 0 and balance > 100000:
            return "Priority retention campaign. Customer has high financial value but low engagement."

        elif products == 1:
            return "Offer relevant additional products and personalized engagement."

        else:
            return "Initiate proactive customer engagement and retention campaign."

    elif risk == "Medium Risk":

        return "Monitor customer activity and provide personalized offers."

    else:

        return "Maintain engagement and consider cross-selling relevant products."


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("📊 Customer Engagement & Retention Analytics")

st.markdown(
    """
    **Behavior-driven customer retention decision support system**

    Analyze customer engagement, product utilization, financial commitment,
    and retention risk.
    """
)


# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Dashboard",
    "👤 Real-Time Assessment",
    "🔎 Customer Analysis",
    "📁 Upload Data"
])


# =========================================================
# TAB 1 - DASHBOARD
# =========================================================

with tab1:

    st.header("📊 Customer Retention Dashboard")

    # -----------------------------
    # SIDEBAR FILTERS
    # -----------------------------

    st.sidebar.header("Filters")

    products = st.sidebar.slider(
        "Number of Products",
        int(df["NumOfProducts"].min()),
        int(df["NumOfProducts"].max()),
        (
            int(df["NumOfProducts"].min()),
            int(df["NumOfProducts"].max())
        )
    )

    balance = st.sidebar.slider(
        "Balance",
        0.0,
        float(df["Balance"].max()),
        (
            0.0,
            float(df["Balance"].max())
        )
    )

    activity = st.sidebar.selectbox(
        "Customer Engagement",
        ["All", "Active", "Inactive"]
    )

    filtered_df = df[
        (df["NumOfProducts"] >= products[0]) &
        (df["NumOfProducts"] <= products[1]) &
        (df["Balance"] >= balance[0]) &
        (df["Balance"] <= balance[1])
    ]

    if activity == "Active":
        filtered_df = filtered_df[
            filtered_df["IsActiveMember"] == 1
        ]

    elif activity == "Inactive":
        filtered_df = filtered_df[
            filtered_df["IsActiveMember"] == 0
        ]

    # -----------------------------
    # KPIs
    # -----------------------------

    col1, col2, col3, col4 = st.columns(4)

    churn_rate = filtered_df["Exited"].mean()

    active_churn = df[
        df["IsActiveMember"] == 1
    ]["Exited"].mean()

    inactive_churn = df[
        df["IsActiveMember"] == 0
    ]["Exited"].mean()

    engagement_ratio = (
        inactive_churn / active_churn
        if active_churn != 0
        else 0
    )

    high_balance = df[
        df["Balance"] > df["Balance"].quantile(0.75)
    ]

    high_balance_disengaged = high_balance[
        high_balance["IsActiveMember"] == 0
    ]

    high_balance_risk = (
        high_balance_disengaged["Exited"].mean()
        if len(high_balance_disengaged) > 0
        else 0
    )

    col1.metric(
        "Churn Rate",
        f"{churn_rate:.2%}"
    )

    col2.metric(
        "Engagement Ratio",
        f"{engagement_ratio:.2f}"
    )

    col3.metric(
        "High Balance Risk",
        f"{high_balance_risk:.2%}"
    )

    col4.metric(
        "Customers",
        len(filtered_df)
    )

    st.divider()

    # -----------------------------
    # CHURN BY PRODUCTS
    # -----------------------------

    st.subheader("📦 Churn by Number of Products")

    product_churn = (
        filtered_df
        .groupby("NumOfProducts")["Exited"]
        .mean()
    )

    st.bar_chart(product_churn)

    # -----------------------------
    # ACTIVITY VS CHURN
    # -----------------------------

    st.subheader("👥 Engagement vs Churn")

    engagement_data = (
        filtered_df
        .groupby("IsActiveMember")["Exited"]
        .mean()
    )

    engagement_data.index = [
        "Inactive",
        "Active"
    ]

    st.bar_chart(engagement_data)

    # -----------------------------
    # CREDIT CARD
    # -----------------------------

    st.subheader("💳 Credit Card Ownership vs Churn")

    card_data = (
        filtered_df
        .groupby("HasCrCard")["Exited"]
        .mean()
    )

    card_data.index = [
        "No Credit Card",
        "Credit Card"
    ]

    st.bar_chart(card_data)

    # -----------------------------
    # HIGH VALUE CUSTOMERS
    # -----------------------------

    st.subheader("⚠️ High-Value Disengaged Customers")

    threshold = df["Balance"].quantile(0.75)

    high_value = df[
        (df["Balance"] >= threshold) &
        (df["IsActiveMember"] == 0)
    ]

    st.dataframe(
        high_value[
            [
                "CreditScore",
                "Geography",
                "Gender",
                "Age",
                "Tenure",
                "Balance",
                "NumOfProducts",
                "HasCrCard",
                "IsActiveMember",
                "EstimatedSalary",
                "Exited"
            ]
        ].head(20),
        use_container_width=True
    )


# =========================================================
# TAB 2 - REAL-TIME ASSESSMENT
# =========================================================

with tab2:

    st.header("👤 Real-Time Customer Retention Assessment")

    st.write(
        "Enter the current customer information to estimate "
        "retention strength and identify potential churn risk."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        credit_score = st.number_input(
            "Credit Score",
            min_value=300,
            max_value=850,
            value=650
        )

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=35
        )

        tenure = st.number_input(
            "Tenure (Years)",
            min_value=0,
            max_value=20,
            value=5
        )

        balance = st.number_input(
            "Account Balance",
            min_value=0.0,
            value=50000.0,
            step=5000.0
        )

    with col2:

        products_input = st.number_input(
            "Number of Products",
            min_value=1,
            max_value=4,
            value=1
        )

        has_card = st.selectbox(
            "Has Credit Card?",
            ["Yes", "No"]
        )

        active_member = st.selectbox(
            "Is Active Member?",
            ["Yes", "No"]
        )

        salary = st.number_input(
            "Estimated Salary",
            min_value=0.0,
            value=50000.0,
            step=5000.0
        )

    st.divider()

    assess = st.button(
        "🔍 Assess Customer",
        type="primary",
        use_container_width=True
    )

    if assess:

        card_value = 1 if has_card == "Yes" else 0

        active_value = 1 if active_member == "Yes" else 0

        retention_score = calculate_retention_score(
            credit_score,
            age,
            tenure,
            balance,
            products_input,
            card_value,
            active_value,
            salary
        )

        risk = get_risk_level(
            retention_score
        )

        engagement = get_engagement_level(
            active_value,
            products_input
        )

        recommendation = get_recommendation(
            risk,
            active_value,
            products_input,
            balance
        )

        st.subheader("📋 Customer Assessment Result")

        r1, r2, r3 = st.columns(3)

        r1.metric(
            "Retention Score",
            f"{retention_score}/100"
        )

        r2.metric(
            "Risk Level",
            risk
        )

        r3.metric(
            "Engagement",
            engagement
        )

        st.divider()

        if risk == "Low Risk":

            st.success(
                "🟢 Customer has relatively strong retention indicators."
            )

        elif risk == "Medium Risk":

            st.warning(
                "🟡 Customer requires monitoring and targeted engagement."
            )

        else:

            st.error(
                "🔴 Customer shows high retention risk."
            )

        st.subheader("💡 Recommended Action")

        st.info(recommendation)

        st.subheader("Customer Profile")

        profile = pd.DataFrame({
            "Attribute": [
                "Credit Score",
                "Age",
                "Tenure",
                "Balance",
                "Products",
                "Credit Card",
                "Active Member",
                "Salary"
            ],

            "Value": [
                credit_score,
                age,
                tenure,
                balance,
                products_input,
                has_card,
                active_member,
                salary
            ]
        })

        st.dataframe(
            profile,
            use_container_width=True,
            hide_index=True
        )


# =========================================================
# TAB 3 - CUSTOMER ANALYSIS
# =========================================================

with tab3:

    st.header("🔎 Customer Analysis")

    st.write(
        "Explore individual customers and their retention indicators."
    )

    customer_index = st.number_input(
        "Enter Customer Row Number",
        min_value=0,
        max_value=len(df) - 1,
        value=0
    )

    customer = df.iloc[customer_index]

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Credit Score",
        customer["CreditScore"]
    )

    c2.metric(
        "Balance",
        f"{customer['Balance']:,.2f}"
    )

    c3.metric(
        "Products",
        customer["NumOfProducts"]
    )

    c4.metric(
        "Active Member",
        "Yes" if customer["IsActiveMember"] == 1 else "No"
    )

    st.subheader("Customer Details")

    st.dataframe(
        customer.to_frame("Value"),
        use_container_width=True
    )


# =========================================================
# TAB 4 - UPLOAD DATA
# =========================================================

with tab4:

    st.header("📁 Upload Customer Data")

    st.write(
        "Upload a CSV file containing customer information "
        "for analysis."
    )

    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:

        uploaded_df = pd.read_csv(
            uploaded_file
        )

        st.success(
            "File uploaded successfully!"
        )

        st.write(
            f"Rows: {uploaded_df.shape[0]}"
        )

        st.write(
            f"Columns: {uploaded_df.shape[1]}"
        )

        st.dataframe(
            uploaded_df.head(20),
            use_container_width=True
        )

        st.subheader("Dataset Summary")

        st.write(
            uploaded_df.describe()
        )