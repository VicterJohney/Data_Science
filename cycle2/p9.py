import numpy as np
  
arr = np.arange(1,6).reshape(1,5)
print("1D arr : \n", arr)

a = np.diag(arr)
print("1D Array Diagonal values : \n", a)
 
arr = np.arange(12).reshape(4, 3)
print("2D arr : \n", arr)

a = np.diag(arr)
print("2D Array diagonal values : \n", a)