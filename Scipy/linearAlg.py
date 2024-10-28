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
     [8,8,9]]
)

print("Printing the Array")
print(arr)
print()

# Finding Determinant
determinant = linalg.det(arr)
print("Determinant:-", determinant)
print()

# Finding Inverse of matrix
inverse_arr = linalg.inv(arr)
print("Inverse of matrix:-")
print(inverse_arr)
print()
print("Matrix - Inverse Product")
print(arr @ inverse_arr) # here we can use @ in matrix multiplication
print()

# eigenValue and eigenVector
array2 = np.array([[0,1,2],[3,4,5],[5,6,7]])

egn_val, egn_vec = linalg.eig(array2)
print(egn_val)
print(egn_vec)

# more 