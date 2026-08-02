# Import Required Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read CSV File

df = pd.read_csv("week4/FastFoodRestaurants.csv")

df = df.fillna(0)


# Restaurant Distribution

plt.figure(figsize=(8,5))
sns.displot(data=df, x="latitude", kde=True)
plt.show()


# Latitude Distribution

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="latitude", bins=30)
plt.title("Latitude Distribution")
plt.show()


# Longitude Distribution

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="longitude", bins=30)
plt.title("Longitude Distribution")
plt.show()


# Country Count

plt.figure(figsize=(10,5))
sns.countplot(data=df, y="country")
plt.title("Country Count")
plt.show()


# Province Count

plt.figure(figsize=(12,5))
sns.countplot(data=df,
              y="province",
              order=df["province"].value_counts().head(15).index)
plt.title("Top Provinces")
plt.show()


# Top Restaurant Chains

plt.figure(figsize=(12,5))
sns.countplot(data=df,
              y="name",
              order=df["name"].value_counts().head(15).index)
plt.title("Top Restaurant Chains")
plt.show()


# Restaurant Locations

plt.figure(figsize=(8,6))
sns.scatterplot(data=df,
                x="longitude",
                y="latitude",
                hue="country")
plt.title("Restaurant Locations")
plt.show()


# Latitude vs Longitude

plt.figure(figsize=(8,6))
sns.regplot(data=df,
            x="longitude",
            y="latitude")
plt.title("Latitude vs Longitude")
plt.show()


# Latitude by Country

plt.figure(figsize=(10,5))
sns.boxenplot(data=df,
              x="country",
              y="latitude")
plt.title("Latitude by Country")
plt.xticks(rotation=45)
plt.show()


# Longitude by Country

plt.figure(figsize=(10,5))
sns.violinplot(data=df,
               x="country",
               y="longitude")
plt.title("Longitude by Country")
plt.xticks(rotation=45)
plt.show()


# Restaurants by Country

country = df["country"].value_counts().reset_index()
country.columns = ["Country","Count"]

plt.figure(figsize=(8,5))
sns.barplot(data=country,
            x="Country",
            y="Count")
plt.title("Restaurants by Country")
plt.show()


# Correlation Heatmap

plt.figure(figsize=(6,5))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="magma")
plt.title("Correlation Heatmap")
plt.show()


# Pair Plot

sns.pairplot(df[[
    "latitude",
    "longitude"
]])
plt.show()


# Joint Plot

sns.jointplot(data=df,
              x="longitude",
              y="latitude",
              kind="hex")
plt.show()


# Rug Plot

plt.figure(figsize=(8,5))
sns.rugplot(data=df,
            x="latitude")
plt.title("Latitude Rug Plot")
plt.show()