import requests
import pandas as pd

# MFAPI URL for HDFC Top 100 Direct Growth
url = "https://api.mfapi.in/mf/125497"

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()

    # Extract NAV history
    nav_data = data["data"]

    # Convert to DataFrame
    df = pd.DataFrame(nav_data)

    # Save CSV
    output_path = "data/raw/HDFC_Top100_Live_NAV.csv"
    df.to_csv(output_path, index=False)

    print("Live NAV data saved successfully!")
    print(df.head())

else:
    print("Failed to fetch data.")
    print("Status Code:", response.status_code)