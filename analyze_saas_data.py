import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("saas_customer_data.csv", parse_dates=["signup_date", "renewal_date"])

# Create SQLite database and load data into it
conn = sqlite3.connect("saas_analytics.db")
df.to_sql("customers", conn, if_exists="replace", index=False)

# 1. Revenue by Plan Type
query1 = """
SELECT plan_type, ROUND(SUM(monthly_revenue), 2) AS total_revenue
FROM customers
GROUP BY plan_type
ORDER BY total_revenue DESC;
"""
revenue_by_plan = pd.read_sql_query(query1, conn)

# 2. Churn Rate by Industry
query2 = """
SELECT industry,
       COUNT(*) AS total_customers,
       SUM(churned) AS churned_customers,
       ROUND(100.0 * SUM(churned) / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY industry
ORDER BY churn_rate DESC;
"""
churn_by_industry = pd.read_sql_query(query2, conn)

# 3. Revenue by Region
query3 = """
SELECT region, ROUND(SUM(monthly_revenue), 2) AS total_revenue
FROM customers
GROUP BY region
ORDER BY total_revenue DESC;
"""
revenue_by_region = pd.read_sql_query(query3, conn)

# 4. Usage Score vs. Churn (for visual correlation)
query4 = """
SELECT usage_score, churned
FROM customers;
"""
usage_churn = pd.read_sql_query(query4, conn)

# Close DB connection
conn.close()

# --- Visualizations ---
sns.set(style="whitegrid")

# Revenue by Plan
plt.figure(figsize=(6, 4))
sns.barplot(data=revenue_by_plan, x="plan_type", y="total_revenue", palette="viridis")
plt.title("Total Revenue by Plan Type")
plt.ylabel("Revenue ($)")
plt.xlabel("Plan Type")
plt.tight_layout()
plt.savefig("screenshots/revenue_by_plan.png")
plt.close()

# Churn by Industry
plt.figure(figsize=(8, 5))
sns.barplot(data=churn_by_industry, x="churn_rate", y="industry", palette="mako")
plt.title("Churn Rate by Industry")
plt.xlabel("Churn Rate (%)")
plt.ylabel("Industry")
plt.tight_layout()
plt.savefig("screenshots/churn_by_industry.png")
plt.close()

# Revenue by Region
plt.figure(figsize=(6, 4))
sns.barplot(data=revenue_by_region, x="region", y="total_revenue", palette="coolwarm")
plt.title("Total Revenue by Region")
plt.ylabel("Revenue ($)")
plt.xlabel("Region")
plt.tight_layout()
plt.savefig("screenshots/revenue_by_region.png")
plt.close()

# Usage vs. Churn Boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(data=usage_churn, x="churned", y="usage_score", palette="Set2")
plt.title("Usage Score by Churn Status")
plt.xticks([0, 1], ["Active", "Churned"])
plt.xlabel("Customer Status")
plt.ylabel("Usage Score")
plt.tight_layout()
plt.savefig("screenshots/usage_vs_churn.png")
plt.close()

print("✅ Analysis complete. Visualizations saved in /screenshots")
