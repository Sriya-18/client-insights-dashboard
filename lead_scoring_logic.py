import pandas as pd
import numpy as np

# Set seed for consistency
np.random.seed(42)

# Define constants
n = 500
industries = ['Finance', 'Healthcare', 'Retail', 'Manufacturing', 'Technology']
regions = ['North America', 'Europe', 'Asia-Pacific', 'Latin America']
ai_levels = ['Yes', 'Partial', 'No']

# Create synthetic dataset
df = pd.DataFrame({
    'Client_ID': range(1, n + 1),
    'Company_Name': [f"Company_{i}" for i in range(1, n + 1)],
    'Industry': np.random.choice(industries, size=n),
    'Region': np.random.choice(regions, size=n),
    'Company_Size': np.random.randint(50, 10000, size=n),
    'Annual_Revenue_Million': np.round(np.random.uniform(5, 500), 2),
    'Growth_Rate_%': np.round(np.random.uniform(-10, 30, size=n), 2),
    'AI_Usage_Level': np.random.choice(ai_levels, size=n, p=[0.4, 0.35, 0.25]),
    'Email_Open_Rate_%': np.round(np.random.uniform(5, 90, size=n), 1),
    'CRM_Score': np.random.randint(0, 100, size=n),
    'PoC_Completed': np.random.choice(['Yes', 'No'], size=n, p=[0.3, 0.7])
})

# Map values to numerical scores
df['AI_Score'] = df['AI_Usage_Level'].map({'Yes': 100, 'Partial': 60, 'No': 20})
df['PoC_Score'] = df['PoC_Completed'].map({'Yes': 100, 'No': 0})

# Normalize fields
df['Growth_Score'] = ((df['Growth_Rate_%'] - df['Growth_Rate_%'].min()) / 
                      (df['Growth_Rate_%'].max() - df['Growth_Rate_%'].min())) * 100

df['Open_Rate_Score'] = df['Email_Open_Rate_%']
df['CRM_Score_Norm'] = df['CRM_Score']

# Calculate final lead score
df['Lead_Score'] = (
    df['AI_Score'] * 0.30 +
    df['Growth_Score'] * 0.25 +
    ((df['Open_Rate_Score'] + df['CRM_Score_Norm']) / 2) * 0.25 +
    df['PoC_Score'] * 0.20
)

# Save to CSV
df.to_csv("Client_Lead_Prioritization_Dataset.csv", index=False)
