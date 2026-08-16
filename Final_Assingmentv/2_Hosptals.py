# Question 2 - Machine Learning
# USA Hospitals Dataset

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("Final_Assingmentv/Hospitals.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

df = df.replace("NOT AVAILABLE", np.nan)

cols = ["POPULATION", "TTL_STAFF", "BEDS", "LATITUDE", "LONGITUDE"]

for col in cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df[cols] = df[cols].replace(-999, np.nan)
df[cols] = df[cols].fillna(df[cols].median())

print(df[cols].describe())

sns.histplot(data=df, x="BEDS", kde=True)
plt.title("Hospital Beds Distribution")
plt.show()

sns.histplot(data=df, x="TTL_STAFF", kde=True)
plt.title("Hospital Staff Distribution")
plt.show()

sns.scatterplot(
    data=df,
    x="POPULATION",
    y="BEDS",
    hue="STATUS"
)
plt.title("Hospital Population and Beds")
plt.show()

sns.boxplot(
    data=df,
    x="STATUS",
    y="BEDS"
)
plt.title("Beds by Hospital Status")
plt.show()

sns.countplot(
    data=df,
    y="TYPE",
    order=df["TYPE"].value_counts().head(8).index
)
plt.title("Most Common Hospital Types")
plt.show()

plt.figure(figsize=(9, 6))
sns.heatmap(
    df[cols].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Hospital Feature Correlation")
plt.show()

X = df[cols].copy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

scores = []

for k in range(2, 7):
    model = KMeans(n_clusters=k, random_state=21, n_init=10)
    labels = model.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    scores.append(score)

print("Silhouette Scores:", scores)

best_k = np.argmax(scores) + 2

print("Best Number of Clusters:", best_k)

kmeans = KMeans(
    n_clusters=best_k,
    random_state=21,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

print(df[cols + ["Cluster"]].head(10))

print(df.groupby("Cluster")[cols].mean())

sns.scatterplot(
    data=df,
    x="BEDS",
    y="TTL_STAFF",
    hue="Cluster",
    palette="Set2"
)
plt.title("Hospital Clusters")
plt.show()

sns.countplot(
    data=df,
    x="Cluster"
)
plt.title("Hospitals in Each Cluster")
plt.show()

cluster_summary = df.groupby("Cluster")[[
    "POPULATION",
    "TTL_STAFF",
    "BEDS"
]].mean()

print("\nCluster Summary")
print(cluster_summary)

print("\nFinal Silhouette Score:",
      silhouette_score(X_scaled, df["Cluster"]))