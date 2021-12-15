import numpy as np;

x = np.arange(1,10).reshape(3,3)
print("Matrix x: \n", x)
# Transposing the Matrix M
y=x.transpose();
print("Transpose of x :\n ",y)
# -1(Transpose)
skew=np.multiply(y,-1);  
print("negative of transpose :\n ",skew)
if x.all() == y.all():
    print("Matrix is symmetric")
else:
    print("Matrix is not symmetric")
if x.all() == ~y.all():
    print("Matrix is skew symmetric")
else:
    print("Matrix is not skew matrix")