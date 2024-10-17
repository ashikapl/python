# Use dot product to demonstrate that any two columns of I3 are orthogonal to each other using NUMPY
import numpy as np

I = np.array([[1,0,0],[0,1,0],[0,0,1]])
print("Identity Matrix:-->")
print(I)
print()

# create vector of each columns from 2D to 1D
print("Vector arrays:-->")
c1 = np.array([1,0,0])
print("c1:- ",c1)
c2 = np.array([0,1,0])
print("c2:- ",c2)
c3 = np.array([0,0,1])
print("c3:- ",c3)

# Dot product of each column with each other
ans1 = np.dot(c1,c2)
print("Ans1::-", ans1)
ans2 = np.dot(c1,c3)
print("Ans2::-", ans2)
ans3 = np.dot(c2,c3)
print("Ans3::-", ans3)

print()
print("All columns in identity Matrix are orthogonal to each other!")