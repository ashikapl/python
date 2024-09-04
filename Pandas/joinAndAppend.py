# Join
import pandas as pd

v1 = pd.DataFrame({'A':[1,2,3,4,5],'B':[11,12,13,14,15]}, index=['a','b','c','d','e'])
v2 = pd.DataFrame({'C':[21,22,23],'D':[31,32,33]}, index=['a','b','c'])

# print(v1.join(v2))

 # inner, outer, left, right with (how) function 
print('Inner:-\n', v1.join(v2, how='inner'))
print('Outer:-\n', v1.join(v2, how='outer'))
print('Left:-\n', v1.join(v2, how='left'))
print('Right:-\n', v1.join(v2, how='right'))

# left suffix and right suffix for same col name
a1 = pd.DataFrame({'a':[1,2,3,4],'b':[10,20,30,40]})
a2 = pd.DataFrame({'c':[11,12,13,14],'b':[22,33,44,55]})
print(a1.join(a2,lsuffix='_1_'))
print(a1.join(a2,rsuffix='_2_'))

# Append function is Removed in pandas in place of append we can use (concat) function
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

df_combined = pd.concat([df1, df2], ignore_index=True)
print(df_combined)


