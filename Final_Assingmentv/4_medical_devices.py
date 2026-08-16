# Question 4 - Deep Learning
# FDA AI Medical Devices Dataset

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Dense

df = pd.read_csv("Final_Assingmentv/fda_ai_medical_devices.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

df["final_decision_date"] = pd.to_datetime(df["final_decision_date"])
df["review_days"] = pd.to_numeric(df["review_days"], errors="coerce")

df = df.dropna(subset=["final_decision_date", "review_days"])

monthly = (
    df.set_index("final_decision_date")
      .resample("ME")["review_days"]
      .mean()
      .reset_index()
)

monthly["review_days"] = monthly["review_days"].interpolate()

print(monthly.head())
print(monthly.describe())

sns.histplot(data=df, x="review_days", bins=30, kde=True)
plt.title("FDA Review Days Distribution")
plt.show()

sns.boxplot(data=df, y="review_days")
plt.title("Review Days Spread")
plt.show()

sns.lineplot(data=monthly, x="final_decision_date", y="review_days")
plt.title("Average FDA Review Days Over Time")
plt.xticks(rotation=45)
plt.show()

sns.histplot(data=monthly, x="review_days", kde=True)
plt.title("Monthly Average Review Days")
plt.show()

values = monthly["review_days"].values.astype(float)

scaler = MinMaxScaler()
scaled = scaler.fit_transform(values.reshape(-1, 1))

look_back = 12

X = []
y = []

for i in range(look_back, len(scaled)):
    X.append(scaled[i-look_back:i, 0])
    y.append(scaled[i, 0])

X = np.array(X)
y = np.array(y)

split = int(len(X) * 0.8)

X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)


rnn = Sequential([
    SimpleRNN(32, activation="tanh",
              input_shape=(look_back, 1)),
    Dense(1)
])

rnn.compile(optimizer="adam", loss="mse")
rnn.fit(X_train, y_train, epochs=25, batch_size=8, verbose=0)

rnn_pred = rnn.predict(X_test, verbose=0)


lstm = Sequential([
    LSTM(32, activation="tanh",
         input_shape=(look_back, 1)),
    Dense(1)
])

lstm.compile(optimizer="adam", loss="mse")
lstm.fit(X_train, y_train, epochs=25, batch_size=8, verbose=0)

lstm_pred = lstm.predict(X_test, verbose=0)


gru = Sequential([
    GRU(32, activation="tanh",
        input_shape=(look_back, 1)),
    Dense(1)
])

gru.compile(optimizer="adam", loss="mse")
gru.fit(X_train, y_train, epochs=25, batch_size=8, verbose=0)

gru_pred = gru.predict(X_test, verbose=0)


actual = scaler.inverse_transform(y_test.reshape(-1, 1))

predictions = {
    "RNN": scaler.inverse_transform(rnn_pred),
    "LSTM": scaler.inverse_transform(lstm_pred),
    "GRU": scaler.inverse_transform(gru_pred)
}

for name, pred in predictions.items():

    mae = mean_absolute_error(actual, pred)
    rmse = np.sqrt(mean_squared_error(actual, pred))

    print("\n", name)
    print("MAE:", mae)
    print("RMSE:", rmse)


results = pd.DataFrame({
    "Actual": actual.flatten(),
    "RNN": predictions["RNN"].flatten(),
    "LSTM": predictions["LSTM"].flatten(),
    "GRU": predictions["GRU"].flatten()
})

print(results.tail(12))

plt.figure(figsize=(12, 6))

plt.plot(results["Actual"], label="Actual")
plt.plot(results["RNN"], label="RNN")
plt.plot(results["LSTM"], label="LSTM")
plt.plot(results["GRU"], label="GRU")

plt.title("FDA Review Days Prediction")
plt.xlabel("Test Period")
plt.ylabel("Average Review Days")
plt.legend()
plt.show()