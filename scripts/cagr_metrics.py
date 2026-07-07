import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/HDFC_Top100_NAV.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"], dayfirst=True)

# Sort by date
df = df.sort_values("date").reset_index(drop=True)


def calculate_cagr(df, years):
    """
    Calculate CAGR for the last 'years' years.
    """
    end_date = df["date"].max()
    start_date = end_date - pd.DateOffset(years=years)

    period_df = df[df["date"] >= start_date]

    if len(period_df) < 2:
        return None

    start_nav = period_df.iloc[0]["nav"]
    end_nav = period_df.iloc[-1]["nav"]

    cagr = (end_nav / start_nav) ** (1 / years) - 1
    return cagr


cagr_1 = calculate_cagr(df, 1)
cagr_3 = calculate_cagr(df, 3)
cagr_5 = calculate_cagr(df, 5)

results = pd.DataFrame({
    "Period": ["1 Year", "3 Years", "5 Years"],
    "CAGR": [cagr_1, cagr_3, cagr_5]
})

results.to_csv("data/processed/cagr_metrics.csv", index=False)

print("CAGR metrics saved successfully!")
print(results)