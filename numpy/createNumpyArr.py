# Create Numpy Array's 
import numpy as np

# #creation
# a = np.array([1,2,3])
# # access of the elements
# print(a)
# # access one by one by using index or by looping
# print(a[0])
# print(a[1])
# print(a[2])

# # size -> in bytes
# print("Size of array:", a.itemsize)

# # check type
# print("Datatype:", a.dtype)

# # check dimenstion
# print("Dimension:", a.ndim)
# b = np.array([[1,2],[3,4],[5,4]])
# print("Dimension:", b.ndim)

# # or we can change datatype also
# c = np.array([12,21,36,45], dtype=str)
# print(c)
# print(c.dtype)
# print("Size of array:", c.itemsize)

# # shape
# print("Shape of array:", c.shape)
# b = np.array([[1,2],[3,4],[5,4]])
# print("Shape of array:", b.shape) # 3 row and 2 column

# # create the zero array with full of zero
# arr = np.zeros((3,4))
# print(arr)
# # create the one array with full of ones
# A = np.ones(4)
# print(A)

# create a array with arange function 
array = np.arange(0,5)
print(array)

array1 = np.arange(1,10,3) # here 1 is starting, 10 is end point and 3 is steps
print(array1)

ar = np.linspace(1,5,8) # it gives any random value in float type between the given range
print(ar)

# we can reshape an array
p = np.array([[1,2,7],[3,4,5],[1,2,3],[1,2,3]])
p.reshape(3,4)
print(p, '\n')

q = np.array([[1,2],[3,4],[5,6]])
print(q.reshape(2,3), '\n')
print(q.ravel()) # here ravel is reshape the array in to original form (in linear form)
print("Min value:",q.min())
print("Max value:",q.max())
print("sum value:",q.sum(axis = 0)) # here we can use axis = 1(row) and axis = 0(col) sum
print("Square root of each element:\n", np.sqrt(q))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.dot(a, b)
print("Dot:",result)  # 1∗4+2∗5+3∗6=32


