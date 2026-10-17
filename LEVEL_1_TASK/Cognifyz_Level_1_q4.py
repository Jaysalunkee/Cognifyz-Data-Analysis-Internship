
# LEVEL 1 - TASK 4: ONLINE DELIVERY
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Dataset .csv")
delivery_counts = df["Has Online delivery"].value_counts()

delivery_percentages = (
    df["Has Online delivery"].value_counts(normalize=True) * 100
)

print("Online Delivery Counts:")
print(delivery_counts)

print("\nOnline Delivery Percentages:")
print(delivery_percentages.round(2))

# Average ratings for restaurants with and without delivery
delivery_ratings = (
    df.dropna(subset=["Has Online delivery", "Aggregate rating"])
      .groupby("Has Online delivery")
      .agg(
          Restaurant_Count=("Restaurant ID", "count"),
          Average_Rating=("Aggregate rating", "mean")
      )
      .reset_index()
)

delivery_ratings["Average_Rating"] = (
    delivery_ratings["Average_Rating"].round(2)
)

print("\nAverage Ratings by Online Delivery Availability:")
print(delivery_ratings.to_string(index=False))

# Delivery percentage chart
delivery_plot = delivery_percentages.reset_index()
delivery_plot.columns = ["Online Delivery", "Percentage"]

plt.figure(figsize=(7, 5))
sns.barplot(
    data=delivery_plot,
    x="Online Delivery",
    y="Percentage"
)
plt.title("Restaurants Offering Online Delivery")
plt.ylabel("Percentage of Restaurants (%)")
plt.tight_layout()
plt.show()

# Average rating chart
plt.figure(figsize=(7, 5))
sns.barplot(
    data=delivery_ratings,
    x="Has Online delivery",
    y="Average_Rating"
)
plt.title("Average Ratings: Online Delivery vs No Delivery")
plt.xlabel("Online Delivery")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()
