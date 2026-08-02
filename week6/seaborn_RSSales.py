# Import Required Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read CSV File

df = pd.read_csv("week4/Real_Estate_Sales_2001-2022_GL-Short (1).csv")

df = df.fillna(0)


# Sale Amount Distribution

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="Sale Amount", kde=True)
plt.title("Sale Amount Distribution")
plt.show()


# Assessed Value Distribution

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="Assessed Value", kde=True)
plt.title("Assessed Value Distribution")
plt.show()


# Property Type Count

plt.figure(figsize=(10,5))
sns.countplot(data=df, y="Property Type")
plt.title("Property Type Count")
plt.show()


# Residential Type Count

plt.figure(figsize=(10,5))
sns.countplot(data=df, y="Residential Type")
plt.title("Residential Type Count")
plt.show()


# Sale Amount by Property Type

plt.figure(figsize=(12,5))
sns.boxplot(data=df,
            x="Property Type",
            y="Sale Amount")
plt.xticks(rotation=45)
plt.title("Sale Amount by Property Type")
plt.show()


# Sale Amount by Residential Type

plt.figure(figsize=(12,5))
sns.violinplot(data=df,
               x="Residential Type",
               y="Sale Amount")
plt.xticks(rotation=45)
plt.title("Sale Amount by Residential Type")
plt.show()


# Sale Amount vs Assessed Value

plt.figure(figsize=(8,5))
sns.scatterplot(data=df,
                x="Assessed Value",
                y="Sale Amount")
plt.title("Assessed Value vs Sale Amount")
plt.show()


# Sale Amount by Year

year_data = df.groupby("List Year")["Sale Amount"].mean().reset_index()

plt.figure(figsize=(10,5))
sns.lineplot(data=year_data,
             x="List Year",
             y="Sale Amount")
plt.title("Average Sale Amount by Year")
plt.show()


# Average Sale Amount by Town

town_data = df.groupby("Town")["Sale Amount"].mean().sort_values(ascending=False).head(15).reset_index()

plt.figure(figsize=(12,6))
sns.barplot(data=town_data,
            x="Town",
            y="Sale Amount")
plt.xticks(rotation=90)
plt.title("Top Towns by Average Sale Amount")
plt.show()


# Top Property Types

property_data = df["Property Type"].value_counts().reset_index()
property_data.columns = ["Property Type","Count"]

plt.figure(figsize=(8,5))
sns.barplot(data=property_data,
            x="Property Type",
            y="Count")
plt.xticks(rotation=45)
plt.title("Property Type Frequency")
plt.show()


# Correlation Heatmap

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# Pair Plot

sns.pairplot(df[[
    "Assessed Value",
    "Sale Amount",
    "Sales Ratio"
]])
plt.show()


# Joint Plot

sns.jointplot(data=df,
              x="Assessed Value",
              y="Sale Amount",
              kind="scatter")
plt.show()


# Regression Plot

plt.figure(figsize=(8,5))
sns.regplot(data=df,
            x="Assessed Value",
            y="Sale Amount")
plt.title("Regression Between Assessed Value and Sale Amount")
plt.show()


# Strip Plot

plt.figure(figsize=(12,5))
sns.stripplot(data=df,
              x="Property Type",
              y="Sale Amount")
plt.xticks(rotation=45)
plt.title("Sale Amount by Property Type")
plt.show()