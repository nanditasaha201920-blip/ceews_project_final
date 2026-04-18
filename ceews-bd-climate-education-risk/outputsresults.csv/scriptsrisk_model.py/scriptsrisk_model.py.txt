import os
import pandas as pd

# 1. Create necessary folders automatically
os.makedirs("data/raw", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# 2. Load data
try:
    df = pd.read_csv("data/raw/district_data.csv")
except FileNotFoundError:
    print("❌ Error: 'data/raw/district_data.csv' not found. Please add your CSV file.")
    exit()

# 3. Comprehensive Risk Formula (Updated for all categories)
# Note: climate_resilience is subtracted as it reduces net risk
df["risk_score"] = (
    (0.3 * df["flood_exposure"]) +
    (0.2 * df["poverty_rate"]) +
    (0.15 * df["food_insecurity"]) +
    (0.15 * df["health_access"]) +
    (0.1 * df["education_risk"]) +
    (0.1 * df["gender_gap"])
) - (0.1 * df["climate_resilience"])

# Ensure score stays within 0-1 range
df["risk_score"] = df["risk_score"].clip(lower=0, upper=1)

# 4. Assign Risk Level
df["risk_level"] = pd.cut(
    df["risk_score"],
    bins=[0, 0.25, 0.5, 1],
    labels=["Low", "Medium", "High"]
)

# 5. Save Output
df.to_csv("outputs/results.csv", index=False)

# 6. Summary Report
summary = df["risk_level"].value_counts().sort_index()

print("✅ Done! File saved in outputs/results.csv")
print("\n--- Risk Level Summary Report ---")
print(summary.to_string())
