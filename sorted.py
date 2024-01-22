import numpy as np 

a = np.array([[1, 4, 2], [3, 4, 6], [0, -1, 5]]) 
# sorted array if we want to sort the array in form of a 1-D array
print ("Array elements in sorted order:\n", np.sort(a,axis=None)) 
#The arange([start,] stop[, step,][, dtype]) : Returns an array with evenly spaced elements as per the interval. The interval mentioned is half-opened i.e. [Start, Stop)

# sort array row-wise if axis is not mentioned then we take it to be zero by default
print ("Row-wise sorted array:\n", np.sort(a, axis = 1)) 

# specify sort algorithm 
print ("Column wise :\n", np.sort(a, axis = 0)) 
#numpy.add is used for element-wise addition, while numpy.sum is used for aggregating values along specified axes or across all axes
print(np.empty([4, 3]))# create a new array of given shape and type, without initializing value
print(np.ones([3,3]))#This function is used to get a new array of given shape and type, filled with ones(1).
print(np.zeros([5,5]))#This function is used to get a new array of given shape and type, filled with zeros(0). 
