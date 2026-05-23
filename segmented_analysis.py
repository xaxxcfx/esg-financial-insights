import pandas as pd

df = pd.read_csv('data/esg_financial_data.csv')

# Group by Industry and check average Revenue and ESG_Overall
industry_trends = df.groupby('Industry')[['Revenue', 'ESG_Overall']].mean()

print("--- Average Financials by Industry ---")
print(industry_trends.sort_values(by='ESG_Overall', ascending=False))
