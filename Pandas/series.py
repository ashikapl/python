# Series in pandas in python
import pandas as pd

x = [112, 14, 12, 35, 11, 85, 99]
var = pd.Series(x)
print(var)
print(type(var))

y = [1,2,3,4,5]
s = pd.Series(y, index = ['a','b','c','d','e']) # we can change index value also 
print(s)

# or can make dict series
z = {"Name":"Komal","LastName":"Sharma","Age":24,"Subject":["Maths","Chemistry","Physics"],"Marks":["54,67,90"]}
series = pd.Series(z)
print(series)
print(type(series))

# we can add to series
a = [14,12,11,10,8,4]
b = [1,2,3,4]
c = pd.Series(a)
d = pd.Series(b)

print(c+d)
print(type(c+d))

# string data 
sr = ['a','b','c','d','e','f']
srs = pd.Series(sr)
print(srs)
print(type(srs))