import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/esg_financial_data.csv')

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['ESG_Overall'], df['Revenue'], alpha=0.5)
plt.title('ESG Overall Score vs. Revenue')
plt.xlabel('ESG Overall Score')
plt.ylabel('Revenue')
plt.savefig('esg_vs_revenue.png')
print("Chart saved as esg_vs_revenue.png")

