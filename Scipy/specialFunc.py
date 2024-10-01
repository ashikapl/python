# Special Function (submodule for mathematical operations)
import numpy as np
import scipy.special as special

# find cube root
print("Cube root:-", special.cbrt(np.array([27,125,9])))

# compute exponent (x**y) eg -(10**2)
print("exp10:-", special.exp10([2,3,5])) # we can exponent only 1 and 10(powers)

# Combinations:: Where->
# N is no. of objects
# k is no. of objects being picked (Order don't matter)
print("Combinations:-", special.comb(20,6))#(N,k)
print("Combinations:-", special.comb(10,3))#(N,k)

# Permutation:: where->
# N is no. of objects
# k is no. of objects being picked (Order matter)
print("Permuataion:-", special.perm(20,4)) # (N,k)
print("Permuataion:-", special.perm(6,4)) # (N,k)