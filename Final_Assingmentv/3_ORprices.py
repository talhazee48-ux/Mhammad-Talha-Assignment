# Question 3 - Deep Learning
# Oregon Hospital Data

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Dense

df = pd.read_csv("Final_Assingmentv/OR_hos_prices1.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

df = df.drop(columns=["Unnamed: 0"], errors="ignore")

num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols].replace([np.inf, -np.inf], np.nan)
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

print(df.isnull().sum())

sns.histplot(data=df, x="X-ray: Chest", kde=True)
plt.title("Chest X-ray Price Distribution")
plt.show()

sns.histplot(data=df, x="Ultrasound", kde=True)
plt.title("Ultrasound Price Distribution")
plt.show()

sns.scatterplot(
    data=df,
    x="X-ray: Chest",
    y="Ultrasound"
)
plt.title("Chest X-ray vs Ultrasound")
plt.show()

sns.boxplot(
    data=df,
    y="MRI: Spine"
)
plt.title("MRI Spine Price Distribution")
plt.show()

plt.figure(figsize=(10, 6))

sns.heatmap(
    df[num_cols].corr(),
    cmap="coolwarm"
)

plt.title("Hospital Procedure Price Correlation")
plt.show()

features = [
    "X-ray: Chest",
    "X-ray: Extremities",
    "Ultrasound",
    "X-ray: Spine",
    "Cardiovascular: Electrocardiography",
    "Colonoscopy",
    "Cardiovascular: Echocardiography",
    "Ultrasound: Obstetrical",
    "MRI: Spine",
    "CT scan with contrast: Abdomen/GI",
    "Mammography",
    "CT scan: Chest"
]

data = df[features].copy()

data = data.apply(pd.to_numeric, errors="coerce")
data = data.fillna(data.median())

scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)

look_back = 5

X = []
y = []

for i in range(look_back, len(scaled)):
    X.append(scaled[i-look_back:i])
    y.append(scaled[i, 0])

X = np.array(X)
y = np.array(y)

split = int(len(X) * 0.8)

X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]


# RNN

rnn = Sequential([
    SimpleRNN(
        32,
        activation="tanh",
        input_shape=(X_train.shape[1], X_train.shape[2])
    ),
    Dense(1)
])

rnn.compile(
    optimizer="adam",
    loss="mse"
)

rnn.fit(
    X_train,
    y_train,
    epochs=25,
    batch_size=8,
    verbose=0
)

rnn_pred = rnn.predict(X_test, verbose=0)


# LSTM

lstm = Sequential([
    LSTM(
        32,
        activation="tanh",
        input_shape=(X_train.shape[1], X_train.shape[2])
    ),
    Dense(1)
])

lstm.compile(
    optimizer="adam",
    loss="mse"
)

lstm.fit(
    X_train,
    y_train,
    epochs=25,
    batch_size=8,
    verbose=0
)

lstm_pred = lstm.predict(X_test, verbose=0)


# GRU

gru = Sequential([
    GRU(
        32,
        activation="tanh",
        input_shape=(X_train.shape[1], X_train.shape[2])
    ),
    Dense(1)
])

gru.compile(
    optimizer="adam",
    loss="mse"
)

gru.fit(
    X_train,
    y_train,
    epochs=25,
    batch_size=8,
    verbose=0
)

gru_pred = gru.predict(X_test, verbose=0)


# Model Results

predictions = {
    "RNN": rnn_pred,
    "LSTM": lstm_pred,
    "GRU": gru_pred
}

for name, pred in predictions.items():

    mae = mean_absolute_error(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))

    print("\n" + name)
    print("MAE:", mae)
    print("RMSE:", rmse)


# Compare Predictions

results = pd.DataFrame({
    "Actual": y_test,
    "RNN": rnn_pred.flatten(),
    "LSTM": lstm_pred.flatten(),
    "GRU": gru_pred.flatten()
})

print(results.head(15))

plt.figure(figsize=(12, 6))

plt.plot(results["Actual"], label="Actual")
plt.plot(results["RNN"], label="RNN")
plt.plot(results["LSTM"], label="LSTM")
plt.plot(results["GRU"], label="GRU")

plt.title("Hospital Price Prediction")
plt.xlabel("Test Records")
plt.ylabel("Scaled Chest X-ray Price")
plt.legend()
plt.show()