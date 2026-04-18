import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Climate–Education Risk Dashboard", layout="wide")

# Title
st.title("🌍 Climate–Education Risk Dashboard (Bangladesh)")

# Load data
try:
    df = pd.read_csv("results.csv")

    # Show total districts
    st.metric("Total Districts", len(df))

    # Show full dataset
    st.subheader("📊 District Data")
    st.dataframe(df)

    # Check if risk_level exists
    if "risk_level" in df.columns:
        st.subheader("⚠️ High Risk Districts")
        high_risk = df[df["risk_level"] == "High"]
        st.dataframe(high_risk)

        st.subheader("📈 Risk Level Summary")
        st.write(df["risk_level"].value_counts())
    else:
        st.warning("Column 'risk_level' not found in dataset.")

except Exception as e:
    st.error(f"Error loading data: {e}")
