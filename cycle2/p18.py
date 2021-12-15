import numpy as np;

A = np.array([[1, 2], [3, 4], [5, 6]])
print("Matrix:\n",A)
# SVD
U, s, VT = np.linalg.svd(A)
print("U:\n", U)
print("Sigma:\n",s)
print("V^T:\n",VT)