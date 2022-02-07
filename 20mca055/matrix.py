import numpy as np
x = np.array([[2, 1, 2],
              [3, 0, 1],
              [1, 1, 1]])
y = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("X matrix : ")
print(x)
print("Y matrix : ")
print(y)
#print(7*x)
#print(y*y*y)
print("7X+Y^3 : ")
d=(7*x)+(y*y*y)
print(d)

print("Multiplied matrix x*y : ")
print(np.dot(x,y))
print("Diagonal elements : ")
print(np.diagonal(d))
print("Rank : ")
print(np.linalg.matrix_rank(d))