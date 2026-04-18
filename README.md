🌍 Climate–Education Risk Dashboard (Bangladesh)
📌 Overview
Flooding in Bangladesh significantly disrupts education, especially in vulnerable communities. This project provides a data-driven system to identify districts at risk of student dropout and socio-economic instability due to climate-related factors.
🎯 Objective
To develop a multi-dimensional risk model that supports early intervention in flood-prone areas, helping policymakers and NGOs prioritize resource allocation for climate resilience and education continuity.
🧠 Methodology
This project utilizes seven key indicators sourced from BBS, INFORM, and WFP (2024-2026):
Flood Exposure (Climate hazard frequency)
Poverty Rate (Economic vulnerability)
Education Risk (Dropout/literacy proxy)
Food Insecurity (Nutritional risk)
Health Access (Healthcare distance/availability)
Gender Gap (Disparities in workforce/schooling)
Climate Resilience (Adaptation funding and infrastructure)
📈 Risk Formula
The model calculates a net risk score where socio-economic hazards are balanced against adaptation efforts:
Risk Score =
(0.3 × Flood) + (0.2 × Poverty) + (0.15 × Food) + (0.15 × Health) + (0.1 × Education) + (0.1 × Gender) − (0.1 × Climate Resilience)
Districts are classified as:
Low Risk: (0.0 - 0.25)
Medium Risk: (0.26 - 0.50)
High Risk: (0.51 - 1.00)
📊 Features & Outputs
Automated Processing: Python scripts to clean data and calculate multi-factor risk.
District Analytics: Full risk breakdown for all 64 districts in CSV format.
Priority Identification: Focused reporting on "High Risk" zones like Kurigram and Bandarban.
Summary Reports: Instant distribution counts of risk levels across the country.
🖥️ Dashboard
The project includes an interactive Streamlit dashboard for visual exploration:
Metric Cards: Real-time summary of national risk averages.
Interactive Charts: Scatter plots showing correlations between Poverty and Flood Exposure.
Search & Filter: Find specific districts or filter by risk category.
Data Export: Download filtered results directly from the UI.
Run Locally
Clone the repository:
bash
git clone https://github.com
cd climate-education-risk-bd
Use code with caution.
Install dependencies:
bash
pip install pandas streamlit plotly
Use code with caution.
Run the analysis script:
bash
python scripts/analysis.py
Use code with caution.
Launch the dashboard:
bash
streamlit run app/dashboard.py
Use code with caution.
📂 Project Structure
data/raw/: Original 64-district CSV.
outputs/: Processed risk results and summary reports.
scripts/: Python logic for risk calculations.
app/: Streamlit dashboard code.
🛡️ Data Sources
BBS (Bangladesh Bureau of Statistics): Poverty Map & Census data.
INFORM Subnational Risk Index: Climate and hazard exposure.
WFP/Green Climate Fund: Food security and adaptation funding metrics.
