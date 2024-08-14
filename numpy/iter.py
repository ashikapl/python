# iteration in Numpy array
import numpy as np

a = np.arange(12).reshape(3,4)

# direct print
print(a)

print('\n')

# row wise print
for row in a:
    print(row)

print('\n')

# line wise print
for row in a:
    for cell in row:
        print(cell)
        
print('\n')
        
# direct line wise print using flatten function
for row in a.flatten():
    print(row)
    
print('\n')

# print col wise 
for col in np.nditer(a,order='F'): # here we can use C inside of F to print in row wise
    print(col)
    
print('\n')
    
# print col wise 
for col in np.nditer(a,order='F', flags=['external_loop']): # here we can use C inside of F to print in row wise
    print(col)
    
print('\n')
    
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = x*x # here it will square all the elements
    
print(a)

print('\n')

# this will create a error in iterating both as together with shapes of (3,4) and (5,1) the shape must have equal rows
# b = np.arange(3,20,4).reshape(5,1)
# print(b)

# print('\n')

# for x,y in np.nditer([a,b]):
#     print(x,y) 

b = np.arange(3,15,4).reshape(3,1)

for x,y in np.nditer([a,b]):
    print(x,y)

