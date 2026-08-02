# Import NumPy

import numpy as np


# Read CSV File

data = np.genfromtxt(
    "week4/FastFoodRestaurants.csv",
    delimiter=",",
    dtype=str,
    skip_header=1,
    filling_values="0",
    invalid_raise=False,
    autostrip=True
)


# Remove Empty Rows

data = data[data[:,0] != ""]


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


# First Column

print(data[:,0])


# Second Column

print(data[:,1])


# Third Column

print(data[:,2])


# First 10 Records

print(data[:10])


# Every Second Record

print(data[::2])


# Every Third Record

print(data[::3])


# Unique Values From First Column

print(np.unique(data[:,0]))


# Sort First Column

print(np.sort(data[:,0]))


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