import numpy as np

x = np.arange(1,10).reshape(3,3)
print(x)

print("Matrix cube using multiply(): \n",np.multiply(x,(x*x)))

print("Matrix cube using pow()): \n",np.power(x,3))

print("Matrix cube using *: \n",x*x*x)

print("Matrix cube using **: \n",x**3)

print("Identity Matrix of 3x3: \n",np.identity(3,dtype=int))

print("each element of the matrix to different powers: \n",np.power(x,x))

y=x
print("X^2 +2Y: \n",np.sum(np.power(x,2),np.multiply(y,2)))