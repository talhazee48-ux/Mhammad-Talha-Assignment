# Heart Disease - Machine Learning

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("Final_Assingmentv/heart_disease_cleveland.csv")

print(df.head(8))
print(df.shape)
print(df.dtypes)
print(df.describe())

print(df.isnull().sum())

df["ca"] = df["ca"].fillna(df["ca"].median())
df["thal"] = df["thal"].fillna(df["thal"].median())

print(df["target"].value_counts())

sns.countplot(data=df, x="target")
plt.title("Heart Disease Cases")
plt.show()

sns.boxplot(data=df, x="target", y="age")
plt.title("Age Compared With Target")
plt.show()

sns.scatterplot(data=df, x="trestbps", y="chol", hue="target")
plt.title("Blood Pressure and Cholesterol")
plt.show()

sns.violinplot(data=df, x="target", y="thalach")
plt.title("Maximum Heart Rate by Target")
plt.show()

plt.figure(figsize=(10, 7))
sns.heatmap(df.corr(), annot=True, cmap="viridis")
plt.title("Feature Relationships")
plt.show()

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=21, stratify=y
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

svm = SVC(kernel="rbf")
knn = KNeighborsClassifier(n_neighbors=7)
gb = GradientBoostingClassifier(random_state=21)

svm.fit(X_train, y_train)
knn.fit(X_train, y_train)
gb.fit(X_train, y_train)

svm_pred = svm.predict(X_test)
knn_pred = knn.predict(X_test)
gb_pred = gb.predict(X_test)

models = {
    "SVM": svm_pred,
    "KNN": knn_pred,
    "Gradient Boosting": gb_pred
}

for name, prediction in models.items():
    print("\n", name)
    print("Accuracy:", accuracy_score(y_test, prediction))
    print(classification_report(y_test, prediction))

cm = confusion_matrix(y_test, gb_pred)

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Gradient Boosting Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()