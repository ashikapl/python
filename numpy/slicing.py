# Slicing and stacking the elements in numpy arrays
import numpy as np

a = np.array([1,2,3,4])
print(a[0:3],'\n') # here 0 is start and 3 is end where 3 index element is not include 

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b[0:2],'\n') # here 0 is 0th row and upto 1st row and 2nd is not include
print(b[0:2,2],'\n') # here 0th row upto 1st row only 2th col elements
print(b[-1], '\n') # means last row only
print(b, '\n')
print(b[:,1:3], '\n') # all row and col start from 1 index
print(b[1:3,:2], '\n') # row start from 1 index upto 2nd index and all columns elements

# iterate to an array
for i in b:
    print(i)
    
# by using flat(function) it print all the elements as a list elements print in output in single-single line
for cell in b.flat:
    print(cell)
    
print('\n')

arr1 = np.arange(6).reshape(2,3)
arr2 = np.arange(6,12).reshape(2,3)
print(arr1, '\n')
print(arr2, '\n')

# here we can arrange this two array in one in vertical or horizontal both order
print(np.vstack((arr1,arr2)), '\n') # here two () backets are needed becoz it is a tuple
print(np.hstack((arr1,arr2)), '\n')

# split the array into two or more array in horizontal or vertical both
ar = np.arange(20).reshape(2,10)
print(ar)

res = np.hsplit(ar,5) # h -> for horizontal
print(res[0], '\n')
print(res[1], '\n')
print(res[2], '\n')
print(res[3], '\n')
print(res[4], '\n')

print(np.vsplit(ar,2),'\n') # v -> for vertical

brr = np.arange(9).reshape(3,3)
print(brr)

print('\n')

crr = brr > 4
print(crr) # here is created a boolean array which given true or false according to the crr condition
print(brr[crr])
brr[crr] = -1 # here it will replace the element in brr array by -1 which are true in crr
print(brr)
