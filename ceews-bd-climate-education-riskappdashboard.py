import streamlit as st
import pandas as pd
import os

# Page setup
st.set_page_config(page_title="Climate–Education Risk Dashboard", layout="wide")

# Title
st.title("🌍 Climate–Education Risk Dashboard (Bangladesh)")
st.markdown("Identifying districts where climate factors impact educational continuity.")

# Dynamically handle path to results.csv
# This looks in the current folder, then the parent folder
file_path = "results.csv" if os.path.exists("results.csv") else "../results.csv"

try:
    df = pd.read_csv(file_path)

    # Risk Score Calculation
    df["risk_score"] = (
        0.4 * df["flood_exposure"] +
        0.3 * df["poverty_rate"] +
        0.3 * df["education_risk"]
    )

    # Risk Level Classification
    df["risk_level"] = pd.cut(
        df["risk_score"],
        bins=[0, 0.3, 0.6, 1],
        labels=["Low", "Medium", "High"]
    )

    # --- Metrics Bar ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Districts", len(df))
    col2.metric("High Risk Areas", len(df[df["risk_level"] == "High"]))
    col3.metric("Avg Risk Score", round(df["risk_score"].mean(), 2))

    # --- Main Data Display ---
    st.subheader("📊 Full District Data")
    st.dataframe(df.style.background_gradient(subset=['risk_score'], cmap='YlOrRd'), use_container_width=True)

    # --- Side-by-Side Analysis ---
    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("⚠️ High Risk Priority")
        high_risk = df[df["risk_level"] == "High"].sort_values("risk_score", ascending=False)
        st.dataframe(high_risk[["district", "risk_score", "flood_exposure"]], use_container_width=True)

    with right_col:
        st.subheader("📈 Risk Level Summary")
        summary = df["risk_level"].value_counts().reindex(["Low", "Medium", "High"])
        st.bar_chart(summary)

except Exception as e:
    st.error(f"❌ Error: {e}")
    st.info("Check if 'results.csv' is in the root directory or the 'outputs' folder.")
