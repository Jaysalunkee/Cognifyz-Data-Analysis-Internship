
# LEVEL 1 - TASK 3: PRICE RANGE DISTRIBUTION
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Dataset .csv")

price_counts = df["Price range"].value_counts().sort_index()

price_percentages = (
    df["Price range"].value_counts(normalize=True)
      .sort_index() * 100
)

price_result = pd.DataFrame({
    "Price Range": price_counts.index,
    "Restaurant Count": price_counts.values,
    "Percentage (%)": price_percentages.values.round(2)
})

print("Price Range Distribution:")
print(price_result.to_string(index=False))

# Bar chart
plt.figure(figsize=(8, 5))
sns.barplot(
    data=price_result,
    x="Price Range",
    y="Restaurant Count"
)
plt.title("Distribution of Restaurants by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# Percentage chart
plt.figure(figsize=(8, 5))
plt.bar(
    price_result["Price Range"].astype(str),
    price_result["Percentage (%)"]
)
plt.title("Percentage of Restaurants by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Percentage (%)")
plt.tight_layout()
plt.show()
