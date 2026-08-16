# Iris Dataset
# Hugging Face to CSV

import pandas as pd
from datasets import load_dataset

data = load_dataset("scikit-learn/iris")

df = data["train"].to_pandas()

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df["Species"].value_counts())

df.to_csv("iris_dataset.csv", index=False)

print("CSV created:", len(df))