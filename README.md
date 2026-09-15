# 📊 Business Data Automation & Reporting System

An automated business sales analysis and reporting system built with Python.

The application reads multiple CSV sales files, cleans and combines the data, calculates business metrics, generates a professional Excel report, and provides an interactive Streamlit dashboard.

---

## 🚀 Features

* Automatically reads multiple CSV files
* Combines sales data from different files
* Cleans and validates sales data
* Calculates total revenue
* Calculates total quantity sold
* Calculates total orders
* Calculates average order value
* Performs product-wise revenue analysis
* Performs category-wise revenue analysis
* Performs monthly revenue analysis
* Identifies top-performing products and categories
* Generates a formatted Excel report
* Creates revenue charts
* Provides an interactive Streamlit dashboard
* Supports filtering by product and category

---

## 🛠️ Technologies Used

* Python
* Pandas
* OpenPyXL
* Matplotlib
* Streamlit

---

## 📁 Project Structure

```text
business-data-automation/
│
├── data/
│   ├── input/
│   └── output/
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── analyzer.py
│   ├── report_generator.py
│   └── dashboard.py
│
├── notebooks/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project directory:

```bash
cd business-data-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Generate Excel Report

Run:

```bash
python src/main.py
```

The generated report will be saved inside:

```text
data/output/sales_report.xlsx
```

The Excel report contains:

* Summary
* Sales Data
* Product Analysis
* Category Analysis
* Monthly Analysis

---

## 📊 Run Interactive Dashboard

Start Streamlit:

```bash
streamlit run src/dashboard.py
```

The dashboard provides:

* Total revenue
* Quantity sold
* Number of orders
* Average order value
* Product revenue analysis
* Category revenue analysis
* Monthly revenue trends
* Interactive filters
* Detailed sales table

---

## 🔄 How It Works

```text
CSV Files
    ↓
Data Loading
    ↓
Data Cleaning
    ↓
Revenue Calculation
    ↓
Business Analysis
    ↓
Excel Report
    ↓
Interactive Dashboard
```

---

## 💡 Business Use Case

Businesses often receive sales information in multiple CSV or Excel files.

Manually combining and analyzing these files can be time-consuming and error-prone.

This project automates that process and converts raw sales data into useful business insights.

It can be adapted for:

* Retail businesses
* Small shops
* E-commerce businesses
* Distributors
* Coaching institutes
* Service businesses
* Small companies

---

## 🔮 Future Improvements

Planned improvements include:

* Database integration
* User authentication
* Cloud deployment
* Automated email reports
* PDF report generation
* More advanced dashboards
* Sales forecasting using machine learning
* Automated anomaly detection

---

## 👨‍💻 Author

**Soumyajeet Kar**

B.Tech CSE (AI) Student

Interested in:

* Python
* Data Analytics
* Artificial Intelligence
* Machine Learning
* Software Development
* AI Engineering

---

## ⭐ Project Goal

This project was built as a practical portfolio project to demonstrate Python development, data processing, automation, analytics, reporting, and dashboard development.
