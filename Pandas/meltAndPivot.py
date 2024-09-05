# Melt for data arranging and reshaping
import pandas as pd

# var = pd.DataFrame({'days':[1,2,3,4,5,6],'Math':[12,13,14,15,16,17],'Bio':[15,13,14,16,17,19]})
# print(pd.melt(var)) # data is mele in vertical order
# print(pd.melt(var, id_vars='days'))
# print(pd.melt(var, var_name='Python'))
# print(pd.melt(var, value_name='Pandas'))

# pivot for data arranging and reshaping
v = pd.DataFrame({'days':[1,2,3,4,5,6],
                  'st_name':['a','b','c','a','b','a'],
                  'math':[45,34,23,45,12,34],
                  'eng':[23,24,22,45,33,44]})

# print(v)

print(v.pivot(index='days', columns='st_name'))
print(v.pivot(index='days', columns='st_name',values='eng'))
print(v.pivot_table(index='days',columns='st_name',aggfunc='sum',margins='True'))
print(v.pivot_table(index='days',columns='st_name',aggfunc='mean',margins='True'))