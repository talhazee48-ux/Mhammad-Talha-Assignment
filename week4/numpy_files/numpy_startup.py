# Import NumPy

import numpy as np


# Read CSV File

data = np.genfromtxt(
    "week4/startup_growth_investment_data.csv",
    delimiter=",",
    dtype=str,
    skip_header=1,
    autostrip=True
)


# Complete Dataset

print(data)


# Dataset Shape

print(data.shape)


# Total Elements

print(data.size)


# Number of Dimensions

print(data.ndim)


# Data Type

print(data.dtype)


# First Five Records

print(data[:5])


# Last Five Records

print(data[-5:])


# First Row

print(data[0])


# Last Row

print(data[-1])


# Startup Names

print(data[:,0])


# Industry Column

print(data[:,1])


# Country Column

print(data[:,6])


# Growth Rate Column

print(data[:,8])


# First Ten Startup Names

print(data[:10,0])


# Every Second Record

print(data[::2])


# Every Third Record

print(data[::3])


# Unique Industries

print(np.unique(data[:,1]))


# Unique Countries

print(np.unique(data[:,6]))


# Sort Startup Names

print(np.sort(data[:,0]))


# Sort Countries

print(np.sort(data[:,6]))


# Investment Amount

investment = data[:,3].astype(float)

print(investment)


# Maximum Investment

print(np.max(investment))


# Minimum Investment

print(np.min(investment))


# Average Investment

print(np.mean(investment))


# Total Investment

print(np.sum(investment))


# Growth Rate

growth = data[:,8].astype(float)

print(growth)


# Maximum Growth Rate

print(np.max(growth))


# Average Growth Rate

print(np.mean(growth))


# Startup With Growth Greater Than 100%

print(np.where(growth > 100))


# Count Non Empty Values

print(np.count_nonzero(data))


# Flatten Dataset

print(data.flatten())


# Transpose Dataset

print(data.T)


# Copy Dataset

copy_data = data.copy()

print(copy_data)


# Compare Original And Copy

print(np.array_equal(data, copy_data))