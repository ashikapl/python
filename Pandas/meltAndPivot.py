# Melt for data arranging and reshaping
import pandas as pd

var = pd.DataFrame({'days':[1,2,3,4,5,6],'Math':[12,13,14,15,16,17],'Bio':[15,13,14,16,17,19]})
print(pd.melt(var)) # data is mele in vertical order
print(pd.melt(var, id_vars='days'))
print(pd.melt(var, var_name='Python'))
print(pd.melt(var, value_name='Pandas'))

# pivot for data arranging and reshaping