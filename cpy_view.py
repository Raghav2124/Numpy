import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.view()#just displays the array 
y=arr.copy()#makes a copy of an orignal array 
print(x)
print(y)
x[0]=55
print(y)
y[0]=66
print(arr)
print(x)
print(y)
print(x.base)#shows the base of the array and tells us wheter it is a copy or not 
print(y.base)
#we can also append in an array using append function
arr1=np.array([1,23,4,5])
arr2=np.array([2,3,4,5])
# appending arr2 to arr1
arr = np.append(arr1, arr2)
print('Array after appending : ', arr)