import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
arr5 = np.concatenate((arr3, arr4), axis=1)#axis =0 means we concatenate column wise and axis =1 means row wise 
print(arr5)
#join using stack 
#Stacking is same as concatenation, the only difference is that stacking is done along a new axis
arr7=np.stack((arr1,arr2))
arr8=np.stack((arr1,arr2),axis=1)
arr9=np.hstack((arr1,arr2))
arr10=np.vstack((arr1,arr2))
print(arr7)
print(arr8)
print(arr9)
print(arr10)