# Import Required Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read CSV File

df = pd.read_csv("week4/RealEstate-USA (1).csv")

df = df.fillna(0)


# House Price Distribution

plt.figure(figsize=(8,5))
sns.displot(data=df, x="price", kde=True)
plt.show()


# House Size Distribution

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="house_size", bins=25)
plt.title("House Size Distribution")
plt.show()


# Bedrooms Frequency

plt.figure(figsize=(8,5))
sns.countplot(data=df, x="bed")
plt.title("Bedrooms Count")
plt.show()


# Bathrooms Frequency

plt.figure(figsize=(8,5))
sns.countplot(data=df, x="bath")
plt.title("Bathrooms Count")
plt.show()


# Price by Bedrooms

plt.figure(figsize=(8,5))
sns.boxenplot(data=df, x="bed", y="price")
plt.title("Price by Bedrooms")
plt.show()


# Price by Bathrooms

plt.figure(figsize=(8,5))
sns.boxplot(data=df, x="bath", y="price")
plt.title("Price by Bathrooms")
plt.show()


# House Size vs Price

plt.figure(figsize=(8,5))
sns.scatterplot(data=df,
                x="house_size",
                y="price",
                hue="bath")
plt.title("House Size vs Price")
plt.show()


# Acre Lot vs Price

plt.figure(figsize=(8,5))
sns.regplot(data=df,
            x="acre_lot",
            y="price")
plt.title("Acre Lot vs Price")
plt.show()


# Average Price by State

state_price = df.groupby("state")["price"].mean().sort_values(ascending=False).head(15).reset_index()

plt.figure(figsize=(12,5))
sns.barplot(data=state_price,
            x="state",
            y="price")
plt.xticks(rotation=90)
plt.title("Average Price by State")
plt.show()


# Houses in Each State

plt.figure(figsize=(12,5))
sns.countplot(data=df,
              y="state",
              order=df["state"].value_counts().head(15).index)
plt.title("Top States")
plt.show()


# House Size by Bedrooms

plt.figure(figsize=(8,5))
sns.violinplot(data=df,
               x="bed",
               y="house_size")
plt.title("House Size by Bedrooms")
plt.show()


# Correlation Heatmap

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="YlGnBu")
plt.title("Correlation Heatmap")
plt.show()


# Pair Plot

sns.pairplot(df[[
    "price",
    "bed",
    "bath",
    "house_size",
    "acre_lot"
]])
plt.show()


# Joint Plot

sns.jointplot(data=df,
              x="house_size",
              y="price",
              kind="hex")

plt.show()


# Rug Plot

plt.figure(figsize=(8,5))
sns.rugplot(data=df, x="price")
plt.title("Price Rug Plot")
plt.show()