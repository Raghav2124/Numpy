import numpy as np 
arr=np.array(25) #0-d array /single element array
arr1=np.array([1,2,3,4,5])#1-D array 
arr2=np.array([[1,2,3],[4,5,6]])#2-D array 
arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])#3-D array 
arrH=np.array([1,2,3,5],ndim=5)#creating an array of higher dimensions  ndmin is used to give the dimensions
# In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, 
# the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.
print(arr)
print(arrH)
print(arr1)
print(arr2)
print(arr3)
print(arr.ndim)#prints the arr dimensions of the current array 
