# Linear Algebra using scipy in python
import numpy as np
import scipy.linalg as linalg

# 3x + 2y = 6
# 4x + 8y = 10

a = np.array(
    [[3,2],
    [4,8]]
)

b = np.array([6,10])

print("Solution:-", linalg.solve(a,b))
print()

arr = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]]
)

print("Printing the Array")
print(arr)
print()

# Finding Determinant
determinant = linalg.det(arr)
print("Determinant:-", determinant)