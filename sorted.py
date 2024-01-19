import numpy as np 

a = np.array([[1, 4, 2], [3, 4, 6], [0, -1, 5]]) 
# sorted array if we want to sort the array in form of a 1-D array
print ("Array elements in sorted order:\n", np.sort(a,axis=None)) 

# sort array row-wise if axis is not mentioned then we take it to be zero by default
print ("Row-wise sorted array:\n", np.sort(a, axis = 1)) 

# specify sort algorithm 
print ("Column wise :\n", np.sort(a, axis = 0)) 

