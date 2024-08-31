# Replace in csv files using pandas functions in python
import pandas as pd

var = pd.read_csv("F:\github\python\Data.csv")
print(var)

# Replace
# replace 1 with 22
print(var.replace(to_replace=1,value=22))

# replace with values(1 to 5 S.No replace with 12)
print(var.replace([1,2,3,4,5],12))
print(var.replace(to_replace="Chaheti", value="Aaradiya"))
print(var.replace([45,50,44],60))

# replace using (regex) function
print(var.replace('[A-za-z]','Aashika',regex = True))
# using dictonary
print(var.replace({'Name':'[A-Z]'},4,regex=True))
# method
print(var.replace('AB+',method='bfill'))
print(var.replace('AB+',method='ffill'))
# using limit
print(var.replace('O+',method='ffill',limit=1))
# using inplace which change in original data file
print(var.replace('Kanak',method='ffill',inplace=True))
