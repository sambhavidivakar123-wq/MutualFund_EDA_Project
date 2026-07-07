import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/HDFC_Top100_NAV.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"], dayfirst=True)

# Sort by date
df = df.sort_values("date")

# Calculate Daily Return
df["daily_return"] = df["nav"].pct_change()

# Calculate Cumulative Return
df["cumulative_return"] = (1 + df["daily_return"]).cumprod()

# Calculate Annualized Volatility
volatility = df["daily_return"].std() * (252 ** 0.5)

# Calculate Annualized Return
annual_return = df["daily_return"].mean() * 252

# Sharpe Ratio
risk_free_rate = 0.065

sharpe_ratio = (annual_return - risk_free_rate) / volatility
# Create a DataFrame with the metrics
results = pd.DataFrame({
    "Metric": [
        "Annual Return",
        "Annual Volatility",
        "Sharpe Ratio"
    ],
    "Value": [
        annual_return,
        volatility,
        sharpe_ratio
    ]
})

# Save to CSV
results.to_csv("data/processed/performance_metrics.csv", index=False)

print("Performance metrics saved successfully!")
print(results)