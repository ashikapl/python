# Standard Deviation and Variance of the data using python
import numpy as np

data = np.array([23,24,25,12,43,23,44,22,21,31])

# Standard deviation is a number that describes how spread out the values are.

# A low standard deviation means that most of the numbers are close to the mean (average) value.

# A high standard deviation means that the values are spread out over a wider range.

# std is function to find standard Deviation
# std is square root of variance
print("Standard Deviation:-", np.std(data)) 

# Variance is another number that indicates how spread out the values are.

# In fact, if you take the square root of the variance, you get the standard deviation!

# Or the other way around, if you multiply the standard deviation by itself, you get the variance!

# var is function to find variance 
print("Variance:-", np.var(data))