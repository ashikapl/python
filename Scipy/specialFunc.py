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

# logsumexpo: compute the log of sum of exponenial of input element
# input: [x1,x2,x3,x4]
# output: loge((e**x1)+(e**x2)+(e**x3)+(e**x4))
print("logsumExpo:-",special.logsumexp([1,2,3,4]))

# Lambert w function
# Defind as the inverse of x*(e^x)
# W(z) is such that z = W(z)*(e^W(z)) where z is a complex number
print("W(5):-",special.lambertw(5))