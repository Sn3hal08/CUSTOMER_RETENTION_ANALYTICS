# 📊 Customer Engagement & Product Utilization Analytics for Retention Strategy

## 📌 Project Overview

Customer retention is an important challenge for banks and financial institutions. Understanding customer behavior, engagement, product usage, and financial commitment can help organizations identify customers who are at risk of leaving and develop effective retention strategies.

This project analyzes customer engagement and product utilization data to identify behavioral patterns associated with customer churn.

The project provides an interactive **Streamlit dashboard** that helps analyze:

* Customer engagement and churn
* Product utilization and product depth
* High-value but disengaged customers
* Customer retention strength
* Customer risk segmentation
* Relationship strength and retention indicators

---

## 🎯 Problem Statement

Banks often have large amounts of customer demographic, financial, and product usage data. However, simply knowing a customer's balance, salary, or demographic information is not enough to understand whether the customer is likely to remain loyal.

This project aims to identify behavioral and relationship patterns that influence customer retention and churn.

The analysis focuses on questions such as:

* Does customer engagement influence churn?
* Does the number of products used affect retention?
* Are high-balance customers always loyal?
* Can disengaged high-value customers be identified?
* Which customer profiles are at higher risk of churn?
* How can banks improve customer retention using behavioral insights?

---

## 🎯 Objectives

The main objectives of this project are:

1. Analyze customer engagement in relation to churn.
2. Measure the impact of product count and product utilization on retention.
3. Identify disengaged but high-value customers.
4. Analyze the relationship between financial commitment and engagement.
5. Develop customer retention and risk indicators.
6. Segment customers according to their retention risk.
7. Provide actionable insights for customer retention strategies.
8. Develop an interactive dashboard for business users.

---

## ✨ Key Features

### 1. Engagement vs Churn Analysis

Analyze the relationship between customer activity and churn.

Customer profiles include:

* Highly Engaged
* Moderate Engagement
* Low Engagement
* High Value At Risk

---

### 2. Product Utilization Analysis

Analyze how the number of products used by customers relates to churn.

The dashboard provides analysis of:

* Customers with single products
* Customers with multiple products
* Product depth
* Churn by number of products

---

### 3. High-Value Disengaged Customer Detection

The system identifies customers who have significant financial balances but are inactive.

These customers may represent potential retention risks because their financial value is high even though their engagement is low.

---

### 4. Retention Strength Scoring

A retention score is generated using behavioral and relationship-related factors such as:

* Customer activity
* Number of products
* Customer tenure

The score is used to categorize customers into different risk levels.

---

### 5. Customer Risk Segmentation

Customers are categorized into:

* 🟢 Low Risk
* 🟡 Medium Risk
* 🔴 High Risk

This helps identify customers who may require targeted retention campaigns.

---

### 6. Interactive Dashboard

The Streamlit dashboard provides interactive filters for:

* Number of products
* Customer balance
* Customer engagement
* Customer risk

Users can explore customer segments and analyze churn patterns dynamically.

---

# 📊 Key Performance Indicators (KPIs)

The project uses several behavioral and retention-related KPIs.

### Engagement Retention Ratio

Measures the relative churn behavior between active and inactive customers.

### Product Depth Index

Analyzes customer product usage and its relationship with churn.

### High-Balance Disengagement Rate

Measures the proportion of high-balance customers who are inactive.

### Credit Card Stickiness

Analyzes churn behavior based on credit-card ownership.

### Relationship Strength Index

Combines customer engagement, product usage, and tenure-related factors to estimate relationship strength.

---

# 📁 Dataset

The project uses a customer banking dataset containing attributes such as:

| Attribute       | Description                   |
| --------------- | ----------------------------- |
| Year            | Dataset year                  |
| CustomerId      | Unique customer identifier    |
| Surname         | Customer surname              |
| CreditScore     | Customer credit score         |
| Geography       | Customer location             |
| Gender          | Customer gender               |
| Age             | Customer age                  |
| Tenure          | Number of years with the bank |
| Balance         | Customer account balance      |
| NumOfProducts   | Number of bank products used  |
| HasCrCard       | Credit card ownership         |
| IsActiveMember  | Customer activity status      |
| EstimatedSalary | Estimated customer salary     |
| Exited          | Customer churn indicator      |

### Target Variable

`Exited`

* `0` → Customer retained
* `1` → Customer churned

---

# 🛠️ Technology Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

### Dashboard

* Streamlit

### Development Tools

* PyCharm / VS Code
* Jupyter Notebook
* Git
* GitHub

---

# 📂 Project Structure

```text
CUSTOMER_RETENTION_ANALYTICS/
│
├── data/
│   └── European_Bank.csv
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── kpi.py
│   └── segmentation.py
│
├── app/
│   └── streamlit_app.py
│
├── notebooks/
│   └── eda.ipynb
│
├── reports/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Sn3hal08/customer-retention-analytics.git
```

Navigate to the project directory:

```bash
cd customer-retention-analytics
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run the Project

Run the Streamlit application using:

```bash
streamlit run app/streamlit_app.py
```

The dashboard will open in your browser.

Usually, Streamlit runs at:

```text
http://localhost:8501
```

---

# 📊 Dashboard Modules

The dashboard contains the following major modules:

### 1. Customer Retention Overview

Provides an overall view of customer churn and engagement.

### 2. Engagement vs Churn

Analyzes whether active and inactive customers have different churn patterns.

### 3. Product Utilization

Shows how product count relates to customer churn.

### 4. High-Value Customer Detector

Identifies customers with high balances and low engagement.

### 5. Retention Risk Segmentation

Categorizes customers based on their retention score.

### 6. Customer Filters

Allows users to analyze specific customer groups using interactive filters.

---

# 🔍 Expected Business Insights

The project is designed to help identify patterns such as:

* Customers with low engagement may require proactive retention campaigns.
* Product usage can be analyzed to understand relationship depth.
* High-balance inactive customers may represent important retention opportunities.
* Customers with weak relationship indicators can be prioritized for engagement.
* Product bundling strategies can potentially improve customer relationship depth.

> Note: Actual insights and conclusions should be based on the results obtained from the dataset rather than assuming a particular relationship before analysis.

---

# 🚀 Future Scope

The project can be further enhanced by adding:

* Machine Learning-based churn prediction
* Customer Lifetime Value prediction
* Explainable AI using SHAP
* Automated retention recommendations
* Real-time customer risk monitoring
* Email/SMS retention campaign integration
* Advanced customer segmentation using clustering
* Deployment using Streamlit Cloud or other cloud platforms
* Role-based dashboards for business users and management

---

# 📈 Project Outcome

This project provides a data-driven approach to understanding customer behavior and identifying potential retention risks.

The interactive dashboard transforms customer data into actionable insights that can support:

* Customer retention
* Product cross-selling
* Customer engagement
* Risk prioritization
* Relationship management
* Data-driven business decisions

---

# 👩‍💻 Author

**Snehal Tembhurne**

MCA | Python | Data Analytics | Machine Learning | IT


---

## ⭐ Project Highlights

**Domain:** Banking & Customer Analytics

**Project Type:** Data Analytics + Business Intelligence + Streamlit Dashboard

**Primary Objective:** Customer Retention & Churn Analysis

**Tools:** Python, Pandas, NumPy, Scikit-learn, Streamlit, Git & GitHub
