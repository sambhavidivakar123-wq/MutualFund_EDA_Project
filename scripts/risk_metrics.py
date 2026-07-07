import pandas as pd
import numpy as np
df = pd.read_csv("data/raw/HDFC_Top100_NAV.csv")

df["date"] = pd.to_datetime(df["date"], dayfirst=True)

df = df.sort_values("date")
df["daily_return"] = df["nav"].pct_change()
df["running_max"] = df["nav"].cummax()

df["drawdown"] = (df["nav"] - df["running_max"]) / df["running_max"]

max_drawdown = df["drawdown"].min()
risk_free_rate = 0.065

annual_return = df["daily_return"].mean() * 252

downside_returns = df.loc[df["daily_return"] < 0, "daily_return"]

downside_std = downside_returns.std() * np.sqrt(252)

sortino_ratio = (annual_return - risk_free_rate) / downside_std
var95 = df["daily_return"].quantile(0.05)
results = pd.DataFrame({
    "Metric": [
        "Maximum Drawdown",
        "Sortino Ratio",
        "Value at Risk (95%)"
    ],
    "Value": [
        max_drawdown,
        sortino_ratio,
        var95
    ]
})
results.to_csv("data/processed/risk_metrics.csv", index=False)

print("Risk metrics saved successfully!")

print(results)
