# Import Required Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read CSV File

df = pd.read_csv("week4/startup_growth_investment_data.csv")

df = df.fillna(0)


# Investment Distribution

plt.figure(figsize=(8,5))
sns.displot(data=df, x="Investment Amount (USD)", kde=True)
plt.show()


# Growth Rate Distribution

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="Growth Rate (%)", bins=25)
plt.title("Growth Rate Distribution")
plt.show()


# Industry Count

plt.figure(figsize=(10,5))
sns.countplot(data=df, y="Industry")
plt.title("Industry Count")
plt.show()


# Country Count

plt.figure(figsize=(10,5))
sns.countplot(data=df, y="Country")
plt.title("Country Count")
plt.show()


# Investment by Industry

plt.figure(figsize=(12,5))
sns.boxenplot(data=df,
              x="Industry",
              y="Investment Amount (USD)")
plt.xticks(rotation=45)
plt.title("Investment by Industry")
plt.show()


# Growth by Industry

plt.figure(figsize=(12,5))
sns.boxplot(data=df,
            x="Industry",
            y="Growth Rate (%)")
plt.xticks(rotation=45)
plt.title("Growth by Industry")
plt.show()


# Investment vs Growth

plt.figure(figsize=(8,5))
sns.scatterplot(data=df,
                x="Investment Amount (USD)",
                y="Growth Rate (%)",
                hue="Country")
plt.title("Investment vs Growth")
plt.show()


# Valuation vs Investment

plt.figure(figsize=(8,5))
sns.regplot(data=df,
            x="Investment Amount (USD)",
            y="Valuation (USD)")
plt.title("Valuation vs Investment")
plt.show()


# Funding Rounds vs Growth

plt.figure(figsize=(8,5))
sns.lineplot(data=df,
             x="Funding Rounds",
             y="Growth Rate (%)")
plt.title("Funding Rounds vs Growth")
plt.show()


# Average Investment by Industry

industry = df.groupby("Industry")["Investment Amount (USD)"].mean().reset_index()

plt.figure(figsize=(12,5))
sns.barplot(data=industry,
            x="Industry",
            y="Investment Amount (USD)")
plt.xticks(rotation=45)
plt.title("Average Investment by Industry")
plt.show()


# Average Growth by Country

country = df.groupby("Country")["Growth Rate (%)"].mean().reset_index()

plt.figure(figsize=(10,5))
sns.barplot(data=country,
            x="Country",
            y="Growth Rate (%)")
plt.xticks(rotation=45)
plt.title("Average Growth by Country")
plt.show()


# Correlation Heatmap

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="Spectral")
plt.title("Correlation Heatmap")
plt.show()


# Pair Plot

sns.pairplot(df[
[
"Investment Amount (USD)",
"Valuation (USD)",
"Funding Rounds",
"Growth Rate (%)"
]])
plt.show()


# Joint Plot

sns.jointplot(data=df,
              x="Investment Amount (USD)",
              y="Valuation (USD)",
              kind="hex")
plt.show()


# Rug Plot

plt.figure(figsize=(8,5))
sns.rugplot(data=df,
            x="Growth Rate (%)")
plt.title("Growth Rate Rug Plot")
plt.show()