import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Dataset .csv")

# Basic data cleaning
df.columns = df.columns.str.strip()

# Convert numeric columns
numeric_cols = [
    "Aggregate rating",
    "Votes",
    "Price range",
    "Longitude",
    "Latitude"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Standardize text columns
text_cols = [
    "City", "Cuisines", "Restaurant Name",
    "Has Online delivery", "Has Table booking"
]

for col in text_cols:
    df[col] = df[col].astype("string").str.strip()

print("Dataset loaded successfully!")
print("Rows and columns:", df.shape)
print("\nFirst five rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())
