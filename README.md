# 📊 SaaS Customer Analytics – Churn & Revenue Insights

This project simulates and analyzes customer behavior for a B2B SaaS company, focusing on **churn risk, revenue trends, and engagement** using SQL and Python.

✅ Designed to showcase **business-driven analytics**  
✅ Built with **realistic, simulated data modeled after enterprise SaaS behavior**  
✅ Ideal for roles like **Sales Business Analyst**, **Data Analyst**, and **Customer Insights Analyst**

> ⚠️ Note: All customer records in this dataset are fully simulated to protect real data. They were generated to realistically reflect patterns common in modern B2B SaaS companies.

---

## 📁 Dataset Overview

**File:** `saas_customer_data.csv`  
**Records:** 30,000 simulated customers  
**Fields include:**

| Column             | Description |
|--------------------|-------------|
| `customer_id`      | Unique ID for each customer |
| `industry`         | Customer industry (Fintech, Healthcare, etc.) |
| `region`           | Global region (NA, EMEA, APAC, LATAM) |
| `signup_date`      | Date the customer first subscribed |
| `plan_type`        | SaaS tier (Basic, Pro, Enterprise) |
| `monthly_revenue`  | Monthly recurring revenue (MRR) |
| `churned`          | Whether the customer churned (1 = yes) |
| `renewal_date`     | Date of renewal or churn |
| `sales_rep`        | Assigned sales team |
| `usage_score`      | Customer usage score (0–100) |
| `nps_score`        | Net Promoter Score (1–10) |

---

## 📌 Key Business Questions Answered

- **Which plans and industries churn the most?**
- **Where is revenue strongest (region, plan)?**
- **Does product usage correlate with retention?**
- **How do sales teams compare in revenue and churn?**

---

## 🧪 Analysis Summary

All analysis performed using **SQLite + pandas** and visualized with **matplotlib / seaborn**.

### 🔁 Churn by Industry

<img src="screenshots/churn_by_industry.png" width="500"/>

---

### 💵 Revenue by Plan

<img src="screenshots/revenue_by_plan.png" width="400"/>

---

### 🌍 Revenue by Region

<img src="screenshots/revenue_by_region.png" width="400"/>

---

### 📉 Usage vs. Churn

<img src="screenshots/usage_vs_churn.png" width="400"/>

---

## 🛠 Tools Used

- Python (pandas, matplotlib, seaborn)
- SQLite (via `sqlite3`)
- Faker (for data simulation)
- Git/GitHub (version control + portfolio)

---

## 🔍 Use Cases

This type of analysis is applicable for:
- **Sales Enablement & Revenue Strategy**
- **Customer Success / Retention Analytics**
- **Market Segmentation**
- **Product Usage Insights**

---

## 🧠 Why This Project?

I designed this project to reflect the kind of analytics that matter to:
- **Customer-centric B2B tech companies**
- Firms like **Gartner**, **Forrester**, or **enterprise SaaS orgs**
- Business leaders making data-driven retention or revenue decisions

> ✅ The data is entirely simulated to avoid any confidentiality issues, while preserving realistic structures and behavior for enterprise SaaS companies.

---

## 🚀 How to Run

1. Clone this repo
2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn faker

