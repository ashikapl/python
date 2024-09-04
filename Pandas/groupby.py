# With the help of groupby function we can group the random data in group 
import pandas as pd

var = pd.DataFrame({'Name':['a','a','b','c','a','d','b','c','a','b','d','c','c'],
                   'Sub_1':[34,65,45,33,44,23,32,35,25,55,66,77,54],
                   'Sub_2':[54,34,25,33,44,53,32,22,26,66,77,76,75]})

# print(var)

# groupby Function to group the data corresponding to Name col
var_new = var.groupby('Name')

# for x,y in var_new:
#     print(x)
#     print(y)
    
# get_group function to print selected data from group
v = var_new.get_group('a')
# print(v)

# mean, median, max, min
print('Mean:-', var_new.mean())
print('Median:-', var_new.median())
print('Max:-', var_new.max())
print('Min:-', var_new.min())