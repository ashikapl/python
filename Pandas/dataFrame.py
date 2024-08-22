# DataFrame in pandas
import pandas as pd

s = {'a':[1,2,3,4,5], 'b':[1,2,3,4,5], 'c':[1,2,3,4,5]}
var = pd.DataFrame(s)
print(var)

x = {1:[11,12,13,14,15],2:[110,112,123,114,115],'a':[11,12,13,14,15]}
var1 = pd.DataFrame(x, columns=[1], index=[1,2,3,4,5])
print(var1)

y = {'a':[1,2,3,4,5], 'b':[11,12,13,14,15], 'c':[0,0,0,0,0]}
var2 = pd.DataFrame(y)
print(var2)
print(type(var2))

z = {'a':pd.Series([12,4,3,14,56,7]),'b':pd.Series([11,34,5,64,6,3])}
var3 = pd.DataFrame(z)
print(var3)

# access
list1 = [[1,2,3,4],[5,6,6,7]]
var4 = pd.DataFrame(list1, index=['a','b'])
print(var4)
print("Value:", var4[1]['a'])