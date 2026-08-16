# Import Required Libraries

import pandas as pd


# Read CSV File

df = pd.read_csv("week4/FastFoodRestaurants.csv" , on_bad_lines='skip')


# Replace Missing Values With 0

df = df.fillna(0)


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


# Restaurant Names

print(df["name"])


# Address Column

print(df["address"])


# City Column

print(df["city"])


# Country Column

print(df["country"])


# Province Column

print(df["province"])


# Website Column

print(df["websites"])


# Unique Restaurant Names

print(df["name"].unique())


# Unique Cities

print(df["city"].unique())


# Unique Countries

print(df["country"].unique())


# Sort Restaurant Names

print(df.sort_values(by="name"))


# Sort Cities

print(df.sort_values(by="city"))


# Count Restaurants In Each City

print(df["city"].value_counts())


# Count Restaurants In Each Country

print(df["country"].value_counts())


# Check Missing Values

print(df.isnull().sum())


# Remove Duplicate Records

print(df.drop_duplicates())


# Restaurants In California

print(df[df["province"] == "CA"])


# Restaurants In New York

print(df[df["city"] == "New York"])


# Dataset Information

df.info()


# Dataset Description

print(df.describe(include="all"))