import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="BD Risk Dashboard", layout="wide")

st.title("🌍 Climate–Education Risk Dashboard (Bangladesh)")

try:
    # Load processed data
    df = pd.read_csv("outputs/results.csv")

    # --- TOP METRICS ---
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Districts", len(df))
    m2.metric("High Risk 🔥", len(df[df["risk_level"] == "High"]))
    m3.metric("Avg Risk Score", round(df["risk_score"].mean(), 2))

    # --- MAIN VIEW ---
    st.subheader("📍 All District Data")
    # Adds a search bar for convenience
    search = st.text_input("Search District:", "")
    if search:
        df_display = df[df["district"].str.contains(search, case=False)]
    else:
        df_display = df
    
    st.dataframe(df_display, use_container_width=True)

    # --- HIGH RISK SECTION ---
    st.divider()
    st.subheader("🚨 Urgent Priority: High Risk Districts")
    high_risk = df[df["risk_level"] == "High"].sort_values("risk_score", ascending=False)
    
    if not high_risk.empty:
        st.table(high_risk[["district", "risk_score", "flood_exposure", "poverty_rate"]])
    else:
        st.write("No high-risk districts identified.")

except FileNotFoundError:
    st.error("🚨 **File Not Found!** Please run your Python analysis script first to generate 'outputs/results.csv'.")
except Exception as e:
    st.error(f"⚠️ An unexpected error occurred: {e}")
