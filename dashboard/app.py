import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

# Page configuration
st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    layout="wide"
)


# Title
st.title("📈 Mutual Fund Performance Analytics Dashboard")


# Load data

nav_df = pd.read_csv("data/raw/HDFC_Top100_NAV.csv")
nav_df["date"] = pd.to_datetime(
    nav_df["date"],
    dayfirst=True
)

nav_df = nav_df.sort_values("date")


summary_df = pd.read_csv(
    "data/processed/performance_summary.csv"
)
summary_df = pd.read_csv(
    "data/processed/performance_summary.csv"
)


# Add KPI calculations here 👇

annual_return = summary_df.loc[
    summary_df["Metric"]=="Annual Return",
    "Value"
].values[0]

sharpe = summary_df.loc[
    summary_df["Metric"]=="Sharpe Ratio",
    "Value"
].values[0]

cagr_5 = summary_df.loc[
    summary_df["Metric"]=="5 Years",
    "Value"
].values[0]
# KPI Cards

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Annual Return",
        f"{annual_return*100:.2f}%"
    )

with col2:
    st.metric(
        "Sharpe Ratio",
        f"{sharpe:.2f}"
    )

with col3:
    st.metric(
        "5 Year CAGR",
        f"{cagr_5*100:.2f}%"
    )


col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "Volatility",
        f"{summary_df.loc[summary_df['Metric']=='Annual Volatility','Value'].values[0]*100:.2f}%"
    )

with col5:
    st.metric(
        "Maximum Drawdown",
        f"{summary_df.loc[summary_df['Metric']=='Maximum Drawdown','Value'].values[0]*100:.2f}%"
    )

with col6:
    st.metric(
        "Sortino Ratio",
        f"{summary_df.loc[summary_df['Metric']=='Sortino Ratio','Value'].values[0]:.2f}"
    )
st.subheader("📌 Investor Insights")

st.write(
    f"""
    **Performance Overview**

    📈 The fund generated an annual return of **{annual_return*100:.2f}%**.

    ⭐ The Sharpe Ratio is **{sharpe:.2f}**, indicating the return generated
    relative to the risk taken.

    🚀 The 5-year CAGR is **{cagr_5*100:.2f}%**, showing the long-term growth
    potential of the investment.

    ⚠️ Risk Assessment

    The fund experienced a maximum drawdown of 
    **{summary_df.loc[summary_df['Metric']=='Maximum Drawdown','Value'].values[0]*100:.2f}%**,
    indicating the possible decline during adverse market conditions.

    📊 Annual volatility is around 
    **{summary_df.loc[summary_df['Metric']=='Annual Volatility','Value'].values[0]*100:.2f}%**,
    representing the fluctuation in NAV returns.
    """
)    

# Sidebar

st.sidebar.header("Navigation")

option = st.sidebar.selectbox(
    "Choose Analysis",
    [
        "NAV Trend",
        "Daily Returns",
        "Risk Metrics",
        "Performance Summary",
        "Advanced Analysis"
    ]
)


# NAV Trend

if option == "NAV Trend":

    st.subheader("NAV Movement Over Time")

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(
        nav_df["date"],
        nav_df["nav"]
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("NAV")
    ax.set_title("Fund NAV Trend")

    st.pyplot(fig)
elif option == "Performance Summary":

    st.subheader("Fund Performance Summary")

    st.dataframe(
        summary_df,
        use_container_width=True
    )
       
    csv = summary_df.to_csv(index=False)

    st.download_button(
        label="Download Performance Report",
        data=csv,
        file_name="mutual_fund_performance_report.csv",
        mime="text/csv"
    )
elif option == "Risk Metrics":

    st.subheader("Risk Analysis")

    risk_df = pd.read_csv(
        "data/processed/risk_metrics.csv"
    )

    st.dataframe(
        risk_df,
        use_container_width=True
    )
    st.subheader("Risk Metrics Visualization")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        risk_df["Metric"],
        risk_df["Value"]
    )

    ax.set_xlabel("Metric")
    ax.set_ylabel("Value")
    ax.set_title("Fund Risk Profile")

    plt.xticks(rotation=45)

    st.pyplot(fig)

    st.subheader("Risk Visualization")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        risk_df["Metric"],
        risk_df["Value"]
    )

    ax.set_ylabel("Value")
    ax.set_title("Risk Metrics Overview")

    plt.xticks(rotation=45)

    st.pyplot(fig)
elif option == "Daily Returns":

    st.subheader("📊 Daily Returns Analysis")

    nav_df["Daily Return"] = nav_df["nav"].pct_change()

    avg_return = nav_df["Daily Return"].mean()
    volatility = nav_df["Daily Return"].std()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Average Daily Return",
            f"{avg_return*100:.4f}%"
        )

    with col2:
        st.metric(
            "Daily Volatility",
            f"{volatility*100:.4f}%"
        )


    st.subheader("Daily Return Distribution")

    fig, ax = plt.subplots(figsize=(10,5))

    ax.hist(
        nav_df["Daily Return"].dropna(),
        bins=50
    )

    ax.set_xlabel("Daily Return")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Daily Returns")

    st.pyplot(fig)

# Risk Metrics

elif option == "Risk Metrics":

    st.subheader("Risk Analysis")

    risk_metrics = summary_df[
        summary_df["Metric"].isin(
            [
                "Maximum Drawdown",
                "Sortino Ratio",
                "Value at Risk (95%)"
            ]
        )
    ]
    st.subheader("Risk Metrics Visualization")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        risk_df["Metric"],
        risk_df["Value"]
    )

    ax.set_xlabel("Risk Metric")
    ax.set_ylabel("Value")
    ax.set_title("Fund Risk Profile")

    plt.xticks(rotation=45)

    st.pyplot(fig)

    st.dataframe(
        risk_metrics,
        use_container_width=True
    )
    st.subheader("Risk Metrics Visualization")

    fig, ax = plt.subplots(figsize=(10,5))

    risk_plot = risk_df.copy()

    ax.bar(
    risk_plot["Metric"],
    risk_plot["Value"]
   )

    ax.set_title("Risk Metrics Overview")
    ax.set_ylabel("Value")

    plt.xticks(rotation=45)

    st.pyplot(fig)

elif option == "Performance Summary":

    st.subheader("Fund Performance Summary")

    st.dataframe(
        summary_df,
        use_container_width=True
    )
elif option == "Advanced Analysis":

    st.subheader("Advanced Fund Analysis")

    nav_df["Daily Return"] = nav_df["nav"].pct_change()

    st.write("### Daily Return Distribution")

    fig, ax = plt.subplots(figsize=(10,5))

    ax.hist(
        nav_df["Daily Return"].dropna(),
        bins=50
    )

    ax.set_xlabel("Daily Return")
    ax.set_ylabel("Frequency")
    ax.set_title("Return Distribution")

    st.pyplot(fig)


    st.write("### Drawdown Analysis")

    cumulative = (1 + nav_df["Daily Return"].fillna(0)).cumprod()

    running_max = cumulative.cummax()

    drawdown = (cumulative - running_max) / running_max


    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(
        nav_df["date"],
        drawdown
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Drawdown")

    ax.set_title("Fund Drawdown")

    st.pyplot(fig)    





