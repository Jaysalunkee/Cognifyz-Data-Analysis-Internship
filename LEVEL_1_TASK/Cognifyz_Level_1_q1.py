
# Top 3 Cuisines
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset .csv")
total_restaurants = len(df)

# Split and count cuisines
cuisines = df["Cuisines"].dropna().str.split(",").explode().str.strip()
top_3 = cuisines.value_counts().head(3)

# Create result
result = pd.DataFrame({
    "Cuisine": top_3.index,
    "Restaurant Count": top_3.values,
    "Percentage (%)": (top_3.values / total_restaurants * 100).round(2)
})

print(result)

# Visualize
result.plot(x="Cuisine", y="Restaurant Count", kind="bar", legend=False)
plt.title("Top 3 Most Common Cuisines")
plt.ylabel("Restaurant Count")
plt.tight_layout()
plt.show()
