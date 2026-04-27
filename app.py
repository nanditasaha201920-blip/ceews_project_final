import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Climate-Education Dashboard", layout="wide")

# Title
st.title("🌍 Climate–Education Risk Dashboard (Bangladesh)")
st.write("A simple data-driven model covering 64 districts.")

# Load data
try:
    df = pd.read_csv("results.csv")
except:
    st.error("Error loading dataset. Make sure 'results.csv' exists.")
    st.stop()

# Show total districts
st.metric("Total Districts", len(df))

# Show dataset
st.subheader("📊 District Data")
st.dataframe(df)

# Risk distribution
st.subheader("📈 Risk Distribution")
st.bar_chart(df["education_risk"].value_counts())

# Filter option
st.subheader("🔍 Filter by Risk Level")
risk_levels = df["education_risk"].unique()

risk = st.selectbox("Select Risk Level", risk_levels)

filtered = df[df["education_risk"] == risk]
st.write(filtered)

# High risk districts
st.subheader("⚠️ High Risk Districts")
high = df[df["education_risk"] == "High"]

if not high.empty:
    st.write(high["district"])
else:
    st.write("No high-risk districts found.")

# Insight
st.subheader("💡 Key Insight")
st.write("Flood-prone and coastal districts show higher education disruption risk.")
