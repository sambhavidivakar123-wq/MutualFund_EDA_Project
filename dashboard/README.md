# 📊 Mutual Fund Performance Analytics Dashboard

## 📌 Project Overview

This project analyzes the historical **HDFC Top 100 Mutual Fund** NAV (Net Asset Value) using **Python, SQL, and Power BI**. The project demonstrates an end-to-end data analytics workflow, including data collection, cleaning, exploratory data analysis (EDA), performance and risk analysis, and the development of an interactive Power BI dashboard.

The objective is to help investors understand fund performance, evaluate investment risk, and visualize historical trends through an interactive dashboard.

---

## 🎯 Objectives

- Analyze historical NAV performance.
- Clean and preprocess financial data.
- Calculate key performance and risk metrics.
- Build an interactive Power BI dashboard.
- Demonstrate end-to-end data analytics skills using Python, SQL, and Power BI.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Power BI
- Git & GitHub
- VS Code

---

# 💼 Skills Demonstrated

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- SQL Database Management
- Financial Data Analysis
- Risk Analysis
- KPI Development
- DAX Measures
- Interactive Dashboard Design
- Data Visualization
- Git Version Control

---

# 📂 Project Structure

```text
MutualFund_EDA_Project/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── compute_metrics.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── Mutual_Fund_Dashboard.pbix
│
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── screenshots/
│
├── README.md
└── requirements.txt
```

---

# 📊 Dashboard Overview

The Power BI dashboard consists of **three interactive pages**.

## 📈 Page 1 – Performance Overview

### KPI Cards
- Total AUM
- Latest NAV
- Average NAV
- Annual Return
- NAV Growth %

### Visualizations
- NAV Trend
- 30-Day Moving Average
- Date Slicer
- Year Slicer

---

## 📈 Page 2 – Fund Performance Analysis

### KPI Cards
- Annual Return
- Annual Volatility
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown

### Visualizations
- Daily Return Trend
- Performance Metrics Comparison
- Date Slicer
- Year Slicer

---

## 📈 Page 3 – NAV Analysis

### KPI Cards
- Latest NAV
- Highest NAV
- Lowest NAV
- Average Daily Return

### Visualizations
- HDFC Top 100 NAV Trend
- Daily NAV Return Analysis
- 30-Day Rolling Volatility
- Date Slicer
- Year Slicer

---

# 📈 Performance Metrics

The following financial metrics were calculated:

- Annual Return
- Annual Volatility
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Value at Risk (95%)
- 1-Year Return
- 3-Year Return
- 5-Year Return

---

# 📊 Power BI Dashboard

## Page 1 – Performance Overview

![Dashboard Overview](screenshots/page1_overview.png)

---

## Page 2 – Fund Performance Analysis

![Performance Analysis](screenshots/page2_performance_analysis.png)

---

## Page 3 – NAV Analysis

![NAV Analysis](screenshots/page3_nav_analysis.png)

---

# 🚀 How to Run

1. Clone this repository.

```bash
git clone <repository-url>
```

2. Navigate to the project folder.

```bash
cd MutualFund_EDA_Project
```

3. Install the required Python libraries.

```bash
pip install -r requirements.txt
```

4. Run the ETL and analytics scripts.

5. Open the Power BI dashboard.

```
dashboard/Mutual_Fund_Dashboard.pbix
```

---

# 📌 Key Insights

- The HDFC Top 100 Mutual Fund has demonstrated positive long-term NAV growth.
- Rolling Volatility highlights periods of increased market uncertainty.
- Daily Return Analysis provides insight into short-term fluctuations.
- Sharpe and Sortino Ratios evaluate risk-adjusted fund performance.
- Maximum Drawdown measures the largest decline from a historical peak.
- Interactive slicers allow users to analyze performance across different time periods.

---

# 💡 Business Value

This dashboard enables investors and analysts to:

- Monitor historical fund performance.
- Compare risk-adjusted returns.
- Identify high-volatility periods.
- Track NAV trends over time.
- Support informed investment decisions using interactive visualizations.

---

# 🔮 Future Enhancements

- Live NAV integration using APIs.
- Automated daily data refresh.
- Portfolio comparison across multiple mutual funds.
- Investment recommendation system.
- Streamlit web application.
- Email-based automated performance reports.

---

# 👩‍💻 Author

**Bijjam Sambhavi**

**Data Analytics Project using Python, SQL, and Power BI**

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!