import numpy as np
c=np.zeros((2))
print(c)#create a array such that elements are zero in it 
#create an array with constant values
d = np.full((3, 3), 6, dtype = 'f') #a 2-D 3*3 matrix 
print(d)
# Create a sequence of integers 
# from 0 to 30 with steps of 5 
f = np.arange(0, 30, 5) 
number = np.arange(10)
number2 = np.arange(5,15)
# Takes 2 input start and stop
# Last number not considered
print(number)
print(number2)
print ("A sequential array with steps of 5:", f)
# Create a sequence of 10 values in range 0 to 5 
g = np.linspace(0, 5, 10) 
print ("A sequential array with 10 values between 0 and 5:", g)
#to flatten an array we can use flatten method to do that 


#sort(),  will sort a specified array.
#This method returns a copy of the array, leaving the original array unchanged.
a = np.array([True, False, True])
print(np.sort(a))
