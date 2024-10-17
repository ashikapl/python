# Demonstrate that each of the columns of I3 has unit norm using NUMPY 
import numpy as np

I = np.array([[1,0,0],[0,1,0],[0,0,1]])
print("Identity Matrix:--> ")
print(I)
print()

# divide all the columns in vector form
c1 = np.array([1,0,0])
print("c1:- ", c1)
c2 = np.array([0,1,0])
print("c2:- ", c2)
c3 = np.array([0,0,1])
print("c3:- ", c3)
print()

# Find the unit norm of each column
norm1 = np.linalg.norm(c1)
print("Norm of c1:- ", norm1)
norm2 = np.linalg.norm(c2)
print("Norm of c2:- ", norm2)
norm3 = np.linalg.norm(c3)
print("Norm of c3:- ", norm3)
print()

unit_norm1 = c1 / norm1
unit_norm2 = c1 / norm1
unit_norm3 = c1 / norm1
print("Unit_Norm of c1:- ", unit_norm1)
print("Unit_Norm of c2:- ", unit_norm1)
print("Unit_Norm of c3:- ", unit_norm1)

# Since the norm of each column vector is 1, we confirm that each column of I3 is indeed a unit vector.
# Hence, the columns are not only orthogonal to each other but also have unit norms.
