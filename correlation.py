import pandas as pd

# Load the data
df = pd.read_csv('data/esg_financial_data.csv')

# Select only the relevant numerical columns for correlation
# (We exclude ID and Year as they aren't useful for performance correlation)
cols = ['Revenue', 'ProfitMargin', 'ESG_Overall', 'CarbonEmissions', 'WaterUsage']
correlation_matrix = df[cols].corr()

print("--- Correlation Matrix: ESG vs Financials ---")
print(correlation_matrix['ESG_Overall'])
