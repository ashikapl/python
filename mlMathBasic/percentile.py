# Percentile 
import numpy as np

# An street the ages of peoples given in the form of array
# Find the percentile that how many people are living at what percentile according to their ages
# the result giving the average value that is less than or equal to the each under the percentile

ages = np.array([4,5,7,8,9,12,15,43,56,77,88,12,11,22,32,21])

# it means 70 people are lesser or equal to the age of 27 living in the street 
print("Percentile:-",np.percentile(ages, 70))
print("Percentile::-", np.percentile(ages, 10))
print("Percentile::-", np.percentile(ages, 90))

