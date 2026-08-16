# Import Required Libraries

import pandas as pd


# Read CSV File

df = pd.read_csv("week4/RealEstate-USA (1).csv" , on_bad_lines='skip')


# Complete Dataset

print(df)


# Dataset Shape

print(df.shape)


# Total Elements

print(df.size)


# Number of Dimensions

print(df.ndim)


# Data Types

print(df.dtypes)


# Column Names

print(df.columns)


# First Five Records

print(df.head())


# Last Five Records

print(df.tail())


# Random Five Records

print(df.sample(5))


# First Row

print(df.iloc[0])


# First Ten Rows

print(df.iloc[:10])


# Price Column

print(df["price"])


# City Column

print(df["city"])


# State Column

print(df["state"])


# House Size Column

print(df["house_size"])


# Unique States

print(df["state"].unique())


# Unique Cities

print(df["city"].unique())


# Sort By Price

print(df.sort_values("price"))


# Highest House Price

print(df["price"].max())


# Lowest House Price

print(df["price"].min())


# Average House Price

print(df["price"].mean())


# Total House Price

print(df["price"].sum())


# Count House Prices

print(df["price"].count())


# Count Houses In Each State

print(df["state"].value_counts())


# Missing Values

print(df.isnull().sum())


# Replace Missing Values

print(df.fillna(0))


# Remove Duplicate Records

print(df.drop_duplicates())


# Houses Greater Than 500000

print(df[df["price"] > 500000])


# Houses With More Than 3 Bedrooms

print(df[df["bed"] > 3])


# Houses With More Than 2 Bathrooms

print(df[df["bath"] > 2])


# Houses In New York

print(df[df["state"] == "New York"])


# Houses In Puerto Rico

print(df[df["state"] == "Puerto Rico"])


# Dataset Information

print(df.info())


# Dataset Description

print(df.describe())