# Handling Missing data in csv file using pandas functions in python
import pandas as pd

var = pd.read_csv("F:\\github\\python\\MissData.csv")
print(var)
print('\n')
# dropna function for removing or deleting
print(var.dropna(axis=0))
# if axis = 0 then all the row which have (NaN) value are removed from the file
# if axis = 1 then all the col which have (NaN) value are removed from the file

# we can use (any) which means any row which has any NaN value in row is removed 
print(var.dropna(how="any")) # all which has NaN value (1,4,5,6)
print('\n')
# or we can use (all) which means any row which has all NaN value is removed
print(var.dropna(how="all")) # here only row 5 is removed
print('\n')

# subset parameter which removed the row corresponding to col name
print(var.dropna(subset=["CGPA"]))
print('\n')

# inplace that gives a new data which has no NaN value if(True)
print(var)
var.dropna(inplace=True)# (Remove in original data) # all the col has NaN value so empty data
print(var)
print('\n')

# thresh which remove the NaN value row as the given parameter
# thresh=N requires that a column has at least N non-NaNs to survive
print("thresh:\n", var.dropna(thresh=4))
print('\n')

# fillna function for putting the data on NaN values
print(var.fillna("Hare Krishna!"))
print('\n')
# by dictionary col wise put data 
print(var.fillna({'Name':'Ram','Year':'Kalyug'}))
print('\n')

# forward filling means previous data copied at the current NaN value
print("Forward-Fill:\n", var.fillna(method="ffill")) # here we can use (axis=1(col) or axis=0(row)) by one col to another col from forward
print('\n')
# backward filling means next value data copied at the curr NaN value
print("Backward-Fill:\n", var.fillna(method="bfill",axis=1))  # here we can use (axis=1(col) or axis=0(row)) by one col to another col from backward
print('\n') 

print(var.fillna("Rama",limit=1)) # it put col wise val if each col 1st value change if limit = 1
print('\n') 
print(var)
var.fillna(5,inplace=False)# put 5 at all the NaN value(change in original Data in file)
print(var)
print('\n') 