import numpy as np
arr=np.array([[1,2,3],
              [4,5,6],
              [8,9,0]])
print(arr.ndim)#used to print the dimensions of array
#o/p: 2

arr1=np.array([[[1,2,3],[4,5,6],[8,9,0],
                [1,2,3],[4,5,6],[8,9,0],
                [1,2,3],[4,5,6],[8,9,0]]])
print(arr1.ndim)