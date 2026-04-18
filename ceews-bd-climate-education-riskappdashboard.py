import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Climate–Education Risk Dashboard", layout="wide")

st.title("🌍 Climate–Education Risk Dashboard (Bangladesh)")
st.markdown("Identifying districts where climate factors impact educational continuity.")

try:
    # Try multiple possible file locations (fixes all your path issues)
    possible_paths = [
        "results.csv",
        "../results.csv",
        "../../results.csv",
        "ceews-bd-climate-education-risk/results.csv"
    ]

    df = None
    for path in possible_paths:
        if os.path.exists(path):
            df = pd.read_csv(path)
            break

    if df is None:
        st.error("results.csv not found in any location")
    else:
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

        st.metric("Total Districts", len(df))

        st.subheader("📊 District Data")
        st.dataframe(df)

        st.subheader("⚠️ High Risk Districts")
        st.dataframe(df[df["risk_level"] == "High"])

        st.subheader("📈 Risk Level Summary")
        st.write(df["risk_level"].value_counts())

except Exception as e:
    st.error(f"Error: {e}")
