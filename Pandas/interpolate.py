# Interpolate function means fill data in NaN value(NULL) in pandas in python

import pandas as pd

var = pd.read_csv("F:\github\python\MissData.csv")
print(var)

# interpolate
print(var.interpolate(method='linear',axis=0))
# we can use limit, limit_direction as(forward,backward,or both), limit_area = (inside,outside)
print(var.interpolate(limit_direction='forward',limit=1))
print(var.interpolate(limit_area="outside")) # no change NaN if(inside) it will change NaN value
# here we can use inplace to fill in original data
print(var)
var.interpolate(limit_area="inside",inplace=True)
print(var)