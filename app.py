import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Climate-Education Dashboard", layout="wide")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_content_code=True)

st.title("🌍 Climate–Education Risk Dashboard (Bangladesh)")

# Load dataset (using the CSV data provided previously)
@st.cache_data
def load_data():
    return pd.read_csv("results.csv")

df = load_data()

# Calculate a Composite Vulnerability Score (Flood + Poverty)
df['vulnerability_score'] = (df['flood_risk'] + df['poverty_rate']) / 2

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Options")
risk_level = st.sidebar.multiselect(
    "Select Education Risk Level",
    options=df["education_risk"].unique(),
    default=df["education_risk"].unique()
)

filtered_df = df[df["education_risk"].isin(risk_level)]

# --- TOP METRICS ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Districts", len(filtered_df))
with col2:
    st.metric("Avg Flood Risk", f"{filtered_df['flood_risk'].mean():.2f}")
with col3:
    st.metric("Avg Poverty Rate", f"{filtered_df['poverty_rate'].mean():.2f}")
with col4:
    critical_count = len(df[df['flood_risk'] >= 0.8])
    st.metric("Critical Flood Zones", critical_count, delta_color="inverse")

# --- VISUALIZATIONS ---
c1, c2 = st.columns(2)

with c1:
    st.subheader("📊 Education Risk Distribution")
    fig_bar = px.bar(
        df["education_risk"].value_counts().reset_index(),
        x='education_risk', 
        y='count',
        color='education_risk',
        color_discrete_map={'High': '#ef553b', 'Medium': '#ffa15a', 'Low': '#636efa'}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with c2:
    st.subheader("📍 Flood vs. Poverty Correlation")
    fig_scatter = px.scatter(
        filtered_df, 
        x="flood_risk", 
        y="poverty_rate", 
        color="education_risk",
        hover_name="district",
        size="vulnerability_score",
        template="plotly_white"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# --- DETAILED DATA ---
st.subheader("🔍 District Exploration")
st.dataframe(filtered_df.sort_values(by="vulnerability_score", ascending=False), use_container_width=True)

# --- KEY INSIGHTS ---
st.info(f"💡 **Key Insight:** Of the {len(df)} districts, **{len(df[df['education_risk'] == 'High'])}** are classified as 'High' education risk, showing a strong link to areas where flood risk exceeds 0.6.")

