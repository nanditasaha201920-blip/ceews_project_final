import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Climate–Education Risk Dashboard", layout="wide")

# Title
st.title("🌍 Climate–Education Risk Dashboard (Bangladesh)")
st.markdown("Identifying districts where climate factors impact educational continuity.")

try:
    # Correct path (go one folder up)
    df = pd.read_csv("../results.csv")

    # Create risk score
    df["risk_score"] = (
        0.4 * df["flood_exposure"] +
        0.3 * df["poverty_rate"] +
        0.3 * df["education_risk"]
    )

    # Create risk level
    df["risk_level"] = pd.cut(
        df["risk_score"],
        bins=[0, 0.3, 0.6, 1],
        labels=["Low", "Medium", "High"]
    )

    # Show total districts
    st.metric("Total Districts", len(df))

    # Show full dataset
    st.subheader("📊 District Data")
    st.dataframe(df)

    # High risk districts
    st.subheader("⚠️ High Risk Districts")
    high_risk = df[df["risk_level"] == "High"]
    st.dataframe(high_risk)

    # Summary
    st.subheader("📈 Risk Level Summary")
    st.write(df["risk_level"].value_counts())

except Exception as e:
    st.error(f"Error loading data: {e}")
