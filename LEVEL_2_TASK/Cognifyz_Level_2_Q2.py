
# Task 2: Cuisine Combination
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Dataset .csv")

# Most common cuisine combinations
print("Top 10 Cuisine Combinations:")
print(df["Cuisines"].value_counts().head(10))

# Average rating of each combination
cuisine_ratings = df.groupby("Cuisines")["Aggregate rating"].mean()

print("\nHighest Rated Cuisine Combinations:")
print(cuisine_ratings.sort_values(ascending=False).head(10))
