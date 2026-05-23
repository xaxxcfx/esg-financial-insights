import pandas as pd

# Load the data
df = pd.read_csv('data/esg_financial_data.csv')

# 1. Check for missing values
print("--- Missing Values ---")
print(df.isnull().sum())

# 2. Get basic statistics
print("\n--- Basic Statistics ---")
print(df.describe())


