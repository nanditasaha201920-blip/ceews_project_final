import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Climate–Education Risk Dashboard", layout="wide")

st.title("🌍 Climate–Education Risk Dashboard (Bangladesh)")
st.markdown("Identifying districts where climate factors impact educational continuity.")

try:
    # 2. Load Data
    df = pd.read_csv("results.csv")

    # 3. Calculate Risk Score & Level
    # Updated weights to match your latest preference
    df["risk_score"] = (
        0.4 * df["flood_exposure"] +
        0.3 * df["poverty_rate"] +
        0.3 * df["education_risk"]
    )

    df["risk_level"] = pd.cut(
        df["risk_score"],
        bins=[0, 0.3, 0.6, 1],
        labels=["Low", "Medium", "High"]
    )

    # 4. Top Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Districts", len(df))
    col2.metric("High Risk Areas", len(df[df["risk_level"] == "High"]))
    col3.metric("Avg Risk Score", round(df["risk_score"].mean(), 2))

    # 5. District Data Table
    st.subheader("📊 Full District Analysis")
    st.dataframe(df.style.background_gradient(subset=['risk_score'], cmap='OrRd'), use_container_width=True)

    # 6. Analysis Sections
    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("⚠️ High Risk Priority List")
        high_risk = df[df["risk_level"] == "High"].sort_values("risk_score", ascending=False)
        st.dataframe(high_risk[["district", "risk_score", "flood_exposure"]], use_container_width=True)

    with right_col:
        st.subheader("📈 Risk Distribution Summary")
        summary = df["risk_level"].value_counts().reindex(["Low", "Medium", "High"])
        st.bar_chart(summary)

except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.info("Check if 'results.csv' exists in the same folder as this script.")
