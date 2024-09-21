# How to find mean median and mode using python 
import numpy as np
import pandas as pd

data = np.array([23,25,35,45,56,54,76,23,55,23,89])

# this inbuilt functions are useful in largeData sets or we can calculate by our self also
# the values are in float numbers
print("Mean:-", np.mean(data)) 
print("Median:-", np.median(data))
 
# in Numpy there is no (mode) inbuilt function to find the mode so we can use pandas 
d = pd.Series(data)
# The reason we use [0] after calling mode() in pandas is that the mode() function returns a Series of all mode values
# If there is only one mode in the dataset, mode() will still return a Series with one element. Using [0] allows us to extract that first element.
print("Mode:-", d.mode()[0])

# Mean --> sum up all the numbers and divide by its count (how many number are there)
# Median --> sort all the numbers then find the middle element if there are two middle element then sum up both and divide by 2
# Mode --> the number which has greater frequency is mode


