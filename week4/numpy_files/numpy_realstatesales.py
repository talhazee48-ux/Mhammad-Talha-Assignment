# Import NumPy

import numpy as np


# Read CSV File

data = np.genfromtxt(
    "week4/Real_Estate_Sales_2001-2022_GL-Short (1).csv",
    delimiter=",",
    dtype=str,
    skip_header=1,
    filling_values="0",
    invalid_raise=False,
    autostrip=True
)


# Replace Empty Values With 0

data[data == ""] = "0"


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


# Serial Number Column

print(data[:,0])


# List Year Column

print(data[:,1])


# Town Column

print(data[:,3])


# Address Column

print(data[:,4])


# Assessed Value Column

print(data[:,5])


# Sale Amount Column

print(data[:,6])


# Property Type Column

print(data[:,8])


# Residential Type Column

print(data[:,9])


# First Ten Records

print(data[:10])


# Every Second Record

print(data[::2])


# Every Third Record

print(data[::3])


# Unique Towns

print(np.unique(data[:,3]))


# Unique Property Types

print(np.unique(data[:,8]))


# Sort Town Names

print(np.sort(data[:,3]))


# Sort Property Types

print(np.sort(data[:,8]))


# Assessed Values

assessed = np.where(data[:,5] == "", "0", data[:,5]).astype(float)

print(assessed)


# Sale Amounts

sales = np.where(data[:,6] == "", "0", data[:,6]).astype(float)

print(sales)


# Maximum Assessed Value

print(np.max(assessed))


# Minimum Assessed Value

print(np.min(assessed))


# Average Assessed Value

print(np.mean(assessed))


# Maximum Sale Amount

print(np.max(sales))


# Minimum Sale Amount

print(np.min(sales))


# Average Sale Amount

print(np.mean(sales))


# Total Sale Amount

print(np.sum(sales))


# Index Of Maximum Sale Amount

print(np.argmax(sales))


# Index Of Minimum Sale Amount

print(np.argmin(sales))


# Sale Amount Greater Than 500000

print(np.where(sales > 500000))


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