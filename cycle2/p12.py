import numpy as np
from numpy import random as r

x = r.randint(100, size=(3, 3))
print ("Square matrix with random numbers: \n",x)

print("Inverse: \n", np.linalg.inv(x))

print("Matrix Rank: \n", np.linalg.matrix_rank(x))

print("Determinant: \n", np.linalg.det(x))

print("Transform matrix into 1D: \n", np.ravel(x))

print("Eigen Value: \n", np.linalg.eig(x))