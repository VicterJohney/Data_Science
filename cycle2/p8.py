import numpy as np
  
arr = np.arange(5)
print("1D arr : \n", arr)

a = np.insert(arr, 1, 9)
print("Array after inserting '9' : \n", a)
 
arr = np.arange(12).reshape(3, 4)
print("2D arr : \n", arr)

a = np.insert(arr, 1, 9, axis = 1)
print("Array after inserting '9' : \n", a)