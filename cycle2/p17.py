import numpy as np;

A=np.array([[2,1,-2],[3,0,1],[1,1,-1]])
b=np.array([[-3],[5],[2]])

print("A:\n",A)
print("b:\n",b)

X=np.multiply((np.linalg.inv(A)),b)
print("X is : \n",X)