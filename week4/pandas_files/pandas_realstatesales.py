# Import Required Libraries

import pandas as pd


# Read CSV File

df = pd.read_csv("week4/Real_Estate_Sales_2001-2022_GL-Short (1).csv" , on_bad_lines='skip')


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


# List Year Column

print(df["List Year"])


# Town Column

print(df["Town"])


# Address Column

print(df["Address"])


# Assessed Value Column

print(df["Assessed Value"])


# Sale Amount Column

print(df["Sale Amount"])


# Property Type Column

print(df["Property Type"])


# Residential Type Column

print(df["Residential Type"])


# Unique Towns

print(df["Town"].unique())


# Unique Property Types

print(df["Property Type"].unique())


# Sort By Sale Amount

print(df.sort_values(by="Sale Amount"))


# Sort By Town

print(df.sort_values(by="Town"))


# Highest Sale Amount

print(df["Sale Amount"].max())


# Lowest Sale Amount

print(df["Sale Amount"].min())


# Average Sale Amount

print(df["Sale Amount"].mean())


# Total Sale Amount

print(df["Sale Amount"].sum())


# Count Sale Records

print(df["Sale Amount"].count())


# Count Houses In Each Town

print(df["Town"].value_counts())


# Check Missing Values

print(df.isnull().sum())


# Remove Duplicate Records

print(df.drop_duplicates())


# Houses Greater Than 500000

print(df[df["Sale Amount"] > 500000])


# Houses In Hartford

print(df[df["Town"] == "Hartford"])


# Dataset Information

df.info()


# Dataset Description

print(df.describe(include="all"))