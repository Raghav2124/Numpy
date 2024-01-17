import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
arr1=np.array([1,2,3,4,5])#1-D array 
arr2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print('5th element on 2nd row: ', arr[1, 4])
print(arr1[1])
print(arr2[0, 1, 2])