# Split numpy array using numpy.split()
# Split numpy array using numpy.array_split()
# Splitting NumPy 2D Arrays
# Split numpy array using numpy.vsplit()
# Split numpy array using numpyhsplit()
# Split numpy arrayusing numpy.dsplit()
import numpy as np
array = np.arange(6)
# Splitting the array into 2 equal parts along the first axis (axis=0)
result = np.split(array, 3)

print("Array:")
print(array)
print("Result after numpy.split():")
print(result)
# Creating a 2D array
array = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])

# Splitting the array into 3 equal parts along the second axis (axis=1)
result = np.split(array, 3, axis = 1)

print("2D Array:")
print(array)
print("\nResult after numpy.split() along axis=1:")
print(result)
# 3,8,4 are one array and similarly others