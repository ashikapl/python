# how to insert and delete in DataFrame in python pandas
# in column of DataFrame to can done this operations

import pandas as pd

var = pd.DataFrame({'A':[1,2,3,4,5],'B':[11,12,13,14,14]})
print(var)
print('\n')

# insert a new column in var dataFrame
var.insert(2,"Python",[10,139,34,66,23]) # here 2 is column no, Python is col name, and in last data
print(var)
print('\n')

var.insert(3, "pandas", var['A']) # here we can copy another data from the given column
print(var)
print('\n')

# delete the data
var1 = var.pop('pandas')
print(var1) ## here we can print the deleted data by storing it into a variable
print('\n')
print(var)
print('\n')

# or can use del keyword
del var['Python']
print(var)
