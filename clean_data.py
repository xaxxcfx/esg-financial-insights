import pandas as pd

df = pd.read_csv('data/esg_financial_data.csv')

# Calculate the mean of the GrowthRate
mean_growth = df['GrowthRate'].mean()

# Fill the missing (NaN) values with the mean
df['GrowthRate'] = df['GrowthRate'].fillna(mean_growth)

# Verify that missing values are now 0
print("--- Missing Values After Cleaning ---")
print(df.isnull().sum())
print("\nNew mean GrowthRate:", df['GrowthRate'].mean())

