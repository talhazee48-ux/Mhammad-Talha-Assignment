# AG News Dataset
# Hugging Face to CSV

import pandas as pd
from datasets import load_dataset

data = load_dataset("szhuggingface/ag_news")

train = data["train_full"].to_pandas()
test = data["test"].to_pandas()

df = pd.concat(
    [train, test],
    ignore_index=True
)

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

print(df["label"].value_counts())

print(df.isnull().sum())

df.to_csv("ag_news_dataset.csv", index=False)

print("CSV created:", len(df))