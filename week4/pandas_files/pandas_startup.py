# Import Required Libraries

import pandas as pd


# Read CSV File

df = pd.read_csv("week4/startup_growth_investment_data.csv")


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


# Startup Name Column

print(df["Startup Name"])


# Industry Column

print(df["Industry"])


# Country Column

print(df["Country"])


# Funding Column

print(df["Investment Amount (USD)"])


# Growth Rate Column

print(df["Growth Rate (%)"])


# Unique Industries

print(df["Industry"].unique())


# Unique Countries

print(df["Country"].unique())


# Sort Startup Names

print(df.sort_values(by="Startup Name"))


# Sort Funding Amount

print(df.sort_values(by="Investment Amount (USD)"))


# Highest Funding

print(df["Investment Amount (USD)"].max())


# Lowest Funding

print(df["Investment Amount (USD)"].min())


# Average Funding

print(df["Investment Amount (USD)"].mean())


# Total Funding

print(df["Investment Amount (USD)"].sum())


# Average Growth Rate

print(df["Growth Rate (%)"].mean())


# Count Startups In Each Country

print(df["Country"].value_counts())


# Check Missing Values

print(df.isnull().sum())


# Remove Duplicate Records

print(df.drop_duplicates())


# Startups With Investment Greater Than 1000000

print(df[df["Investment Amount (USD)"] > 1000000])


# Dataset Information

df.info()


# Dataset Description

print(df.describe(include="all"))