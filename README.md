# 🛍️ Retail Data Platform

> An end-to-end Data Engineering project that extracts, validates, cleans, transforms, and loads retail sales data into SQLite while providing business insights through an interactive Power BI dashboard.

---

# 📖 Project Overview

Retail businesses generate thousands of transactions every day. Raw retail datasets often contain duplicate records, missing values, invalid quantities, inconsistent pricing, and poor data quality that make analysis unreliable.

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline built using Python. The pipeline automates the process of extracting raw retail data, validating data quality, cleaning invalid records, performing business transformations, storing the cleaned data into a SQLite database, exporting processed datasets for reporting, and finally creating an interactive Power BI dashboard for business analysis.

This project simulates a real-world data engineering workflow and demonstrates the complete journey from raw data to business insights.

---

# 🎯 Objectives

- Build a complete ETL pipeline
- Validate raw retail data
- Clean and transform data
- Store processed data into SQLite
- Generate ETL logs
- Export processed data
- Build an interactive Power BI Dashboard
- Demonstrate an end-to-end Data Engineering workflow

---

# 🏗️ Project Architecture

```text
                 Online Retail.xlsx
                         │
                         ▼
                ┌─────────────────┐
                │    Extract      │
                └─────────────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    Validate     │
                └─────────────────┘
                         │
                         ▼
                ┌─────────────────┐
                │      Clean      │
                └─────────────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Transform     │
                └─────────────────┘
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
   SQLite Database              Processed CSV
          │                             │
          └──────────────┬──────────────┘
                         ▼
                 Power BI Dashboard
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Processing | Pandas |
| Database | SQLite |
| Data Visualization | Power BI |
| Logging | Python Logging |
| Version Control | Git |
| Repository Hosting | GitHub |

---

# 📂 Project Structure

```text
Retail-Data-Platform/

├── data/
│   ├── raw/
│   │   └── Online Retail.xlsx
│   │
│   ├── processed/
│   │   └── retail_cleaned.csv
│   │
│   └── archive/
│
├── database/
│   └── retail.db
│
├── images/
│   ├── dashboard_page1.png
│   └── dashboard_page2.png
│
├── logs/
│   └── etl.log
│
├── scripts/
│   ├── extract.py
│   ├── validate.py
│   ├── clean.py
│   ├── transform.py
│   └── logger.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🔄 ETL Workflow

## 📥 Extract

- Read the Online Retail Excel dataset.
- Load data into a Pandas DataFrame.

---

## ✅ Validate

The validation process checks:

- Required columns
- Duplicate records
- Missing values
- Negative quantities
- Negative prices
- Invalid data types

---

## 🧹 Clean

The cleaning process performs:

- Remove duplicate rows
- Remove invalid transactions
- Handle missing values
- Standardize data

---

## ⚙️ Transform

New business features are generated:

- Revenue
- Order Month
- Order Year
- Order Day
- Weekend Indicator
- High Value Order Flag

---

## 💾 Load

The processed dataset is:

- Loaded into SQLite
- Exported as a cleaned CSV
- Ready for Power BI reporting

---

# ✨ Features

- End-to-End ETL Pipeline
- Data Validation
- Data Cleaning
- Feature Engineering
- SQLite Database Storage
- CSV Export
- Logging
- Interactive Power BI Dashboard
- Modular Python Scripts

---

# 📊 Power BI Dashboard

## Executive Dashboard

Displays:

- Total Revenue
- Total Customers
- Total Orders
- Total Products
- Monthly Revenue Trend
- Revenue by Country

![Executive Dashboard](images/dashboard_page1.png)

---

## Product Analysis Dashboard

Displays:

- Top 10 Revenue Generating Products
- Product Analysis

![Product Dashboard](images/dashboard_page2.png)

---

# 📈 Business Insights

The dashboard helps answer business questions such as:

- What is the total revenue generated?
- Which countries generate the highest revenue?
- Which products contribute the most revenue?
- How does revenue change month by month?
- How many customers and products are involved?

---

# 📌 Skills Demonstrated

### Data Engineering

- ETL Pipeline Development
- Data Validation
- Data Cleaning
- Data Transformation
- Data Loading

### Python

- Pandas
- Functions
- Modular Programming
- Logging
- Exception Handling

### Database

- SQLite
- SQL Storage

### Business Intelligence

- Power BI
- KPI Cards
- Line Charts
- Bar Charts
- Interactive Dashboards

---

# 🚀 Future Improvements

- PostgreSQL Database
- Apache Airflow Scheduling
- Docker
- AWS S3
- AWS Glue
- Amazon Redshift
- Incremental ETL
- Star Schema Data Warehouse
- Fact & Dimension Tables

---

# ▶️ How to Run

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Retail-Data-Platform.git
```

## Navigate to the project

```bash
cd Retail-Data-Platform
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the ETL pipeline

```bash
python main.py
```

---

# 📸 Output

The project generates:

- Cleaned Retail Dataset
- SQLite Database
- ETL Logs
- Interactive Power BI Dashboard

---

# 👤 Author

**Meer Hyder Siddiqui**

Aspiring Data Engineer

GitHub: https://github.com/YOUR_USERNAME

---

# ⭐ If you found this project useful, consider giving it a Star.