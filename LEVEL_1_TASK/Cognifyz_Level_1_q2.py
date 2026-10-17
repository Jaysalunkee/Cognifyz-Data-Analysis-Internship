
# LEVEL 1 - TASK 2: CITY ANALYSIS

# City with the highest number of restaurants
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Dataset .csv")

city_counts = df["City"].value_counts()

print("City with the Most Restaurants:")
print(city_counts.head(10))

# Average rating and restaurant count by city
city_analysis = (
    df.dropna(subset=["City", "Aggregate rating"])
      .groupby("City")
      .agg(
          Restaurant_Count=("Restaurant ID", "count"),
          Average_Rating=("Aggregate rating", "mean")
      )
      .reset_index()
)

city_analysis["Average_Rating"] = (
    city_analysis["Average_Rating"].round(2)
)

city_analysis = city_analysis.sort_values(
    "Average_Rating", ascending=False
)

print("\nTop 10 Cities by Average Rating:")
print(city_analysis.head(10).to_string(index=False))

# City with highest average rating
highest_rated_city = city_analysis.iloc[0]

print("\nCity with Highest Average Rating:")
print(highest_rated_city)

# Visualize top 10 cities by restaurant count
top_cities = city_counts.head(10).reset_index()
top_cities.columns = ["City", "Restaurant_Count"]

plt.figure(figsize=(11, 6))
sns.barplot(
    data=top_cities,
    x="Restaurant_Count",
    y="City"
)
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.tight_layout()
plt.show()

# Visualize average rating for the top 10 cities by count
top_city_names = city_counts.head(10).index
rating_plot = city_analysis[
    city_analysis["City"].isin(top_city_names)
].sort_values("Average_Rating", ascending=False)

plt.figure(figsize=(11, 6))
sns.barplot(
    data=rating_plot,
    x="Average_Rating",
    y="City"
)
plt.title("Average Ratings in the Top 10 Cities by Restaurant Count")
plt.xlabel("Average Rating")
plt.ylabel("City")
plt.tight_layout()
plt.show()
