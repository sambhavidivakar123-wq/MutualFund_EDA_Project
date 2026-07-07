import pandas as pd

# Read all metrics
performance = pd.read_csv("data/processed/performance_metrics.csv")
risk = pd.read_csv("data/processed/risk_metrics.csv")
cagr = pd.read_csv("data/processed/cagr_metrics.csv")

# Rename columns for consistency
performance.columns = ["Metric", "Value"]
risk.columns = ["Metric", "Value"]

# Convert CAGR table to Metric-Value format
cagr = cagr.rename(columns={"Period": "Metric", "CAGR": "Value"})

# Merge all metrics
summary = pd.concat([performance, risk, cagr], ignore_index=True)

# Save
summary.to_csv("data/processed/performance_summary.csv", index=False)

print("Performance Summary Report Created Successfully!\n")
print(summary)