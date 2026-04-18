import streamlit as st
import pandas as pd

st.title("Climate–Education Risk Dashboard (Bangladesh)")

try:
    df = pd.read_csv("outputs/results.csv")
    st.dataframe(df)
except Exception as e:
    st.error(f"Error loading file: {e}")import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(page_title="Bangladesh Risk Dashboard", layout="wide")

st.title("🇧🇩 Bangladesh Climate & Socio-Economic Risk Tracker")

# Load Data
try:
    df = pd.read_csv("outputs/results.csv")

    # --- TOP METRICS ---
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Districts", len(df))
    m2.metric("High Risk 🔥", len(df[df["risk_level"] == "High"]))
    m3.metric("Avg Poverty", f"{round(df['poverty_rate'].mean() * 100, 1)}%")
    m4.metric("Avg Resilience 🛡️", round(df['climate_resilience'].mean(), 2))

    # --- ANALYTICS TABS ---
    tab1, tab2, tab3 = st.tabs(["📋 Data Table", "📉 Risk Correlations", "📊 Risk Distribution"])

    with tab1:
        st.subheader("Interactive District Registry")
        search = st.text_input("Quick Search District:", "")
        display_df = df[df["district"].str.contains(search, case=False)] if search else df
        st.dataframe(display_df.style.background_gradient(cmap='Reds', subset=['risk_score']), use_container_width=True)

    with tab2:
        st.subheader("Deep Dive: Vulnerability vs. Resilience")
        col_left, col_right = st.columns(2)

        with col_left:
            # Scatter Plot: Poverty vs Flood
            fig1 = px.scatter(df, x="flood_exposure", y="poverty_rate", 
                             color="risk_level", hover_name="district",
                             title="Poverty vs. Flood Exposure",
                             labels={"flood_exposure": "Flood Risk", "poverty_rate": "Poverty Rate"})
            st.plotly_chart(fig1, use_container_width=True)

        with col_right:
            # Scatter Plot: Resilience vs Risk
            fig2 = px.scatter(df, x="climate_resilience", y="risk_score", 
                             color="risk_level", size="food_insecurity", hover_name="district",
                             title="Resilience Impact on Risk Score",
                             labels={"climate_resilience": "Adaptation Funding", "risk_score": "Final Risk"})
            st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        st.subheader("Total Count by Risk Category")
        risk_counts = df["risk_level"].value_counts().reindex(["Low", "Medium", "High"])
        st.bar_chart(risk_counts, color="#ff4b4b")

    # --- DOWNLOAD BUTTON ---
    st.sidebar.header("Data Tools")
    csv = df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button("📥 Download Analysis CSV", csv, "bd_risk_analysis.csv", "text/csv")

except FileNotFoundError:
    st.error("🚨 Run your analysis script first to generate 'outputs/results.csv'!")
