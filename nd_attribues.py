import numpy as np
print("i-d array")
n1=np.array([1,2,3,4])
print(n1)
print("2-d array")
n2=np.array([[1,2,3],[4,5,6]])
print(n2)
print("3-d array")
n3=np.array([ [ [1,2],[3,4],[5,6],[7,8]]])
print(n3)
print("n-d array")
n=np.array([ [ [ [ [ 1,2],[2,3]]]]])
print(n)
#limit for n d is 32
print("------------------------------------------------------------------")
print(n1.itemsize,n2.itemsize)#item space 4 bytes
print(n1.shape,n2.shape)#row,col
print(n1.ndim,n2.ndim)#dimension
print(n1.size,n2.size)#number of elements