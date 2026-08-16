# Diabetes Dataset
# Hugging Face to CSV

import pandas as pd
from datasets import load_dataset

data = load_dataset("Humayd/Diabetes")

df = data["train"].to_pandas()

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df["Outcome"].value_counts())

print(df.isnull().sum())

df.to_csv("diabetes_dataset.csv", index=False)

print("CSV created:", len(df))