import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/esg_financial_data.csv')

# Fill missing values to ensure the heatmap is accurate
df['GrowthRate'] = df['GrowthRate'].fillna(df['GrowthRate'].mean())

# Select only numerical columns for the heatmap
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Create a correlation matrix
corr_matrix = numeric_df.corr()

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of ESG and Financial Data')
plt.savefig('correlation_heatmap.png')
print("Heatmap saved as correlation_heatmap.png")
