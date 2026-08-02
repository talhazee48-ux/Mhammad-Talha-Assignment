# Import NumPy

import numpy as np


# Read CSV File

data = np.genfromtxt("week4/RealEstate-USA (1).csv",
                     delimiter=",",
                     dtype=str,
                     skip_header=1)


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


# First Column

print(data[:,0])


# Price Column

print(data[:,2])


# City Column

print(data[:,7])


# State Column

print(data[:,8])


# First 10 Prices

print(data[:10,2])


# Every Second Record

print(data[::2])


# Every Third Record

print(data[::3])


# Unique States

print(np.unique(data[:,8]))


# Unique Cities

print(np.unique(data[:,7]))


# Sort States

print(np.sort(data[:,8]))


# Sort Cities

print(np.sort(data[:,7]))


# Search Houses Greater Than 500000

price = data[:,2].astype(float)

print(np.where(price > 500000))


# Maximum Price

print(np.max(price))


# Minimum Price

print(np.min(price))


# Average Price

print(np.mean(price))


# Sum of Prices

print(np.sum(price))


# Index of Maximum Price

print(np.argmax(price))


# Index of Minimum Price

print(np.argmin(price))


# House Size Column

house = np.where(data[:,10] == "", "0", data[:,10]).astype(float)

print(house)


# Maximum House Size

print(np.max(house))


# Average House Size

print(np.mean(house))


# Flatten Dataset

print(data.flatten())


# Transpose Dataset

print(data.T)


# Reshape First 60 Elements

print(data.flatten()[:60].reshape(10,6))


# Copy Dataset

copy_data = data.copy()

print(copy_data)


# Count Non Empty Values

print(np.count_nonzero(data))


# Join First Two Rows

print(np.concatenate((data[0],data[1])))


# Vertical Stack

print(np.vstack((data[0],data[1])))


# Horizontal Stack

print(np.hstack((data[0],data[1])))


# Compare Original and Copy

print(np.array_equal(data,copy_data))