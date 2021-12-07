import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("1D arr : \n", arr)

a = np.sum(arr)
print("1D Array Sum : \n", a)
 
arr = np.array( [ [1, 2, 3],[ 4, 5, 6],[7, 8, 9] ])
print("2D arr : \n", arr)

a = np.sum(arr)
print("2D Array Sum : \n", a)