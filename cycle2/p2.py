import numpy as np
x=np.array([[1+2j,1+3j,2+3j],[5+6j,3+8j,4+5j]])
print(x)
print("Number of Rows and Columns:",x.shape)
print("Reshaped matrix is:")
print(x.reshape(3,2))
print("Dimensions:",x.ndim)