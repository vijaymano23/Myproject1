import numpy as np

# 1D array:
a=[1,2,3,4,5]
arr1=np.array([1,2,3,4,5])
print('The numpy array is:', arr1)
print('The type of the numpy array is:', type(arr1))
print('The list is:', a)
print('The type of the list is:', type(a))
print(type(a)) 
print(arr1.dtype)

# 2D array:
a=[1,2,3,4]
b=[5,6,7,8]
c=[9,10,11,12]
arr=np.array([a,b,c])
print('The 2D numpy array is:', arr)
print('The shape of 2d:',arr.shape)
print(arr1.size)
print(arr.dtype)

# crearing a nd array using fromiter():
str='welcome to python programming'
arr2=np.fromiter(str,dtype='U1',count=len(str))     
print(arr2) 

#numpy array using arange():                 
print(np.arange(2,6,2,dtype='float32')) 

# linespace() method:
ret_value=np.linspace(1,10,5,dtype='int32',retstep=True)  
print(ret_value)   

# numpy arrray using zeros() method:
print(np.empty((2,3),dtype='int32',order='c'))


print(np.zeros((2,3),dtype='int32',order='c'))

print(np.ones((3,3),dtype='int32',order='c'))

print(np.full((3,3),7,dtype='int32',order='c'))
