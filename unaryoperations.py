import numpy as np 
  
arr = np.array([[1, 5, 6], [4, 7, 2], [3, 1, 9]]) 
b=np.array([])
# maximum element of array 
print ("Largest element is:", arr.max()) 
print ("Row-wise maximum elements:", arr.max(axis = 1) ) #print the max element row wise
print("column-wise maximum elements: ",arr.max(axis=0))#prints max element column -wise from every column
#same can be said about minimum function
print("smallest element is : ",arr.min())
print("smallest row-wise element is : ",arr.min(axis=1))
print("smallest column-wise element is : ",arr.min(axis=0))
# sum of array elements 
print ("Sum of all array elements:", arr.sum()) 
