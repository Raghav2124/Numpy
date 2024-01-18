import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)#change the size of array but the changes need to be stored as they are not done on the main array as it is a copy  
print(newarr)
newarr1=arr.reshape(2,3,2)
print(newarr1)
ne=arr.reshape(2,2,-1)#-1 can also be used for array flatening
#we can also use unkonwn dimensions but only for one parameter and that  is -1 and this is calculated by the compiler 
# also make sure that number of elements remain same because if not then there will be a error
print(arr)
for x in newarr:
    print(x)
for x in newarr:
    for y in x:
        print(y)
#alternatye method 
for x in np.nditer(arr):
    print(x)
for x in np.nditer(arr,flags=["buffered"],op_dtypes=['S']):
    print(x)
for i,x in np.ndenumerate(arr):
    print(i,x)