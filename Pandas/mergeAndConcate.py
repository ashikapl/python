# Merge and Concatenate two DataFrame 
import pandas as pd

# Merge 

# # to merge two dataFrame we want a common series(col) in both 
# var1 = pd.DataFrame({'A':[1,2,3,4,5],'B':[11,12,13,14,15]})
# var2 = pd.DataFrame({'A':[1,2,3,4,5],'C':[21,22,23,24,25]})

# # Both give same output
# res = pd.merge(var1,var2) # or we can use (pd.merge(var2,var1))
# res1 = pd.merge(var1,var2,on='A')
# print(res)
# print(res1)

# # if the dataFrame is not same the
# v1 = pd.DataFrame({'a':[1,2,3,4],'b':[11,12,13,14]})
# v2 = pd.DataFrame({'a':[1,2,3,6],'c':[45,44,34,12]})
# print(pd.merge(v1,v2)) # then it will print only the same data

# # outer, inner, left, right (how) function
# # we can use indicator function to show how the data merge
# print(pd.merge(v1,v2,how='inner'))
# print(pd.merge(v1,v2,how='outer', indicator='_merge_'))
# print(pd.merge(v1,v2,how='left'))
# print(pd.merge(v1,v2,how='right'))

# # if the dataFrame Col names are same or data are same then we can use this (left_index, or right_index)
# a1 = pd.DataFrame({'a':[1,2,3,4],'b':[5,6,7,8]})
# a2 = pd.DataFrame({'a':[1,2,3,5],'b':[1,1,1,1]})
# print(pd.merge(a1,a2,left_index=True,right_index=True))

# # Suffixes
# print(pd.merge(a1,a2,left_index=True,right_index=True,suffixes=('name','id')))

# Concate ->(Concatenate)

s1 = pd.Series([1,2,3,4])
s2 = pd.Series([5,6,7,8,9])

s = pd.concat([s1,s2])
print(s)

v1 = pd.DataFrame({'a':[1,2,3,4],'b':[5,6,7,8]})
v2 = pd.DataFrame({'a':[1,2,3,4],'c':[5,6,7,8]})
print(pd.concat([v1,v2],axis=0,join='inner')) # or can use axis = 1

print(pd.concat([v1,v2],axis=0,keys=['v1','v2'])) # or can use axis = 1