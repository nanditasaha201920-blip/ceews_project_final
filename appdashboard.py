import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Climate–Education Risk Dashboard", layout="wide")

st.title("🌍 Climate–Education Risk Dashboard (Bangladesh)")
st.markdown("Identifying districts where climate factors impact educational continuity.")

try:
    # Get current file directory
    current_dir = os.path.dirname(__file__)

    # Go up TWO levels to reach repo root
    root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))

    # Build full path to results.csv
    file_path = os.path.join(root_dir, "results.csv")

    # Load data
    df = pd.read_csv(file_path)

    # Risk score
    df["risk_score"] = (
        0.4 * df["flood_exposure"] +
        0.3 * df["poverty_rate"] +
        0.3 * df["education_risk"]
    )

    # Risk level
    df["risk_level"] = pd.cut(
        df["risk_score"],
        bins=[0, 0.3, 0.6, 1],
        labels=["Low", "Medium", "High"]
    )

    st.metric("Total Districts", len(df))

    st.subheader("📊 District Data")
    st.dataframe(df)

    st.subheader("⚠️ High Risk Districts")
    st.dataframe(df[df["risk_level"] == "High"])

    st.subheader("📈 Risk Level Summary")
    st.write(df["risk_level"].value_counts())

except Exception as e:
    st.error(f"Error: {e}")
