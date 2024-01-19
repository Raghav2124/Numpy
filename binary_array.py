import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[10,11,12],[13,14,15],[16,17,18]])
#add two arrays but they should have same dimensions otherwise it will show an array 
print("Array sum: ",a+b)
#subtract two arrays
print("Array subtraction: ",b-a)
#multiplication of two arrays
print("This does  Multiplication elementwise: ",a*b)
#if we want to do multiplication matrix wise we will need dot function
print("Matrix Multiplication: ",a.dot(b))
