#dtype  returns the data type of the array
import numpy as np
arr=np.array([1,2,3,4])
print(arr.dtype)
arr1=np.array([2,3,4,5],dtype='S')
print(arr1)

arr2 = np.array([1, 2, 3, 4], dtype='i4')
print(arr2.dtype)
arr3 = np.array([1.1, 2.1, 3.1])
#alternate method to define the data type 
newarr = arr3.astype('i')#The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
print(newarr)
print(newarr.dtype)
