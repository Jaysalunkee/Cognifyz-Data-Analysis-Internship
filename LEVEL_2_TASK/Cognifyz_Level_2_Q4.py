
# Task 4: Restaurant Chains
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Dataset .csv")

# Count restaurant outlets
chains = df["Restaurant Name"].value_counts()

print("Top 10 Restaurant Chains by Outlet Count:")
print(chains.head(10))

# Calculate average rating and total votes
chain_analysis = df.groupby("Restaurant Name").agg({
    "Aggregate rating": "mean",
    "Votes": "sum"
})

# Keep names with multiple outlets
chain_analysis["Outlet Count"] = chains
chain_analysis = chain_analysis[
    chain_analysis["Outlet Count"] > 1
]

print("\nTop Rated Restaurant Chains:")
print(
    chain_analysis.sort_values(
        "Aggregate rating", ascending=False
    ).head(10).round(2)
)

# Most popular chains by total votes
print("\nMost Popular Restaurant Chains:")
print(
    chain_analysis.sort_values(
        "Votes", ascending=False
    ).head(10)
)
