# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr1[0:2, 2])

print(arr[1:5])
print(arr[4:])
print(arr[:4])

print(arr[1:5:2])#Use the step value to determine the step of the slicing: