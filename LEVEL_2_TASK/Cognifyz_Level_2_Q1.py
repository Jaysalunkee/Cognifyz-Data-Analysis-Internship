
# Task 1: Restaurant Ratings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Dataset .csv")
# Rating distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Aggregate rating"], bins=5, edgecolor="black")
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.show()

# Most common rating range
rating_range = pd.cut(df["Aggregate rating"], bins=5)
print("Most common rating range:")
print(rating_range.value_counts().idxmax())

# Average votes
print("Average votes:", round(df["Votes"].mean(), 2))
