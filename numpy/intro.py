# Numpy (Numerical Python) is extremely popular module in python . It is used in scientific computing
# Numpy's most useful feature is n-dimensional array (ndarray's)
# Benifits ->> Less memory, fast and convinient
import numpy as np
import time
import sys

# Less memory (numpy array then python list) Example--

# Python list 
l = range(1000)
print("Length of List:", sys.getsizeof(1)*len(l))

# Numpy array
a = np.arange(1000)
print("Numpy array length:", a.size*a.itemsize)

# fast and convinient then python list

# Python list
SIZE = 100000
list1 = range(SIZE)
list2 = range(SIZE)

# Numpy array
a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

start = time.time()
result = [(x+y) for x,y in zip(list1,list2)]
print("Python list time:", (time.time()-start)*1000) # multi by 1000 becoz it convert into milliseconds

start = time.time()
result = a1 + a2
print("Numpy array time:", (time.time()-start)*1000)

