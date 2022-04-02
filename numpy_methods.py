"""
using numpy methods we can create arrays without using array() module
ones(row,col)---------creates row matrix only ones
full()---------creates
fill()---------
zeros()--------
eye()----------
diag()---------
arange()------
linspace()-----
random()-------
"""
import numpy as np
print("------------------------arange-------------------")
#arange prints array
arr=np.arange(1,10)
print(arr)
arr_step=np.arange(1,10,2)
print(arr_step)
print("-------------------------linspace-----------------")
#linspace distributes 5 values with in the range equally..
#retstep is false by default....difference is printed
arr1=np.linspace(1,10,5,retstep=True)
print(arr1)
print("-------------------------ones-----------------------")
#by default dtype=none
#creates only ones
arr2=np.ones([5],dtype=int)#row
print(arr2)
arr3=np.ones([3,4])#row,col
print(arr3)
arr4=np.ones([2,2,2],dtype=int)#no.of matriv=ces,row,col
print(arr4)
print("---------------------------zeros------------------")
#same like ones
#creates only zeroes
arr5=np.zeros(5,dtype=int)
print(arr5)
arr6=np.zeros([2,3],dtype=int)
print(arr6)
print("--------------------------eye----------------------")
#identity matrix
i=np.eye(4)
print(i)
print("-------------------------full-----------------------")

