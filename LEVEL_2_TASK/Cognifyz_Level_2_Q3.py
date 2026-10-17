
# Task 3: Geographic Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Dataset .csv")

geo_df = df.dropna(subset=["Longitude", "Latitude"])

plt.figure(figsize=(10, 6))
plt.scatter(
    geo_df["Longitude"],
    geo_df["Latitude"],
    alpha=0.5
)

plt.title("Restaurant Locations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Cities with the most restaurants
print("Top 10 Cities:")
print(df["City"].value_counts().head(10))
