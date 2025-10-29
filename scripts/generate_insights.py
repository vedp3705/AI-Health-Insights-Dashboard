import pandas as pd
import json
import os

DATA_PATH = "data/Dataset_Health.csv"
OUTPUT_PATH = "dashboard/insights.json"

def generate_insights():
    df = pd.read_csv(DATA_PATH)
    
    summary = df.describe().to_dict()

    if "Steps_Day_1" in df.columns:
        correlations = df.corr(numeric_only=True)["Steps_Day_1"].sort_values(ascending=False).to_dict()
    else:
        correlations = {}

    insights = {"row_count": len(df), "column_count": len(df.columns), "summary": summary, "correlations": correlations, "top_features": list(correlations.keys())[:5] if correlations else []}

    os.makedirs("dashboard", exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(insights, f, indent=4)
    print(f"Insights saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_insights()
