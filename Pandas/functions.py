# Function in Pandas Python
import pandas as pd

csv_1 = pd.read_csv("F:\github\python\Student.csv")
print(csv_1)

print('\n')
print("This function shows index range::-",csv_1.index)
print('\n')
print("col names::-", csv_1.columns)
print('\n')
print(csv_1.describe()) # it shows mean, count, minVal, maxVal, std, 25%, 50%, 75%(only for numeric values)
print('\n')
print(csv_1.head(4)) # it show 0 to 3 index data form starting
print('\n')
print(csv_1.tail(3)) # it show 4th (last) to 2nd index data from ending
print('\n')
print(csv_1[:3]) # silcing
print('\n')
print(csv_1[2:5])
print('\n')

# convert it index into array
print(type(csv_1))
print(csv_1.index.array)

# convert it into numpy array
v = csv_1.to_numpy()
print(v)
print('\n')
 
import numpy as np
w = np.array(csv_1)
print(w)

print('\n')
# print(csv_1.sort_index(axis=0, ascending=False)) # rows are sorting in descending order
csv_1.loc[0,"Name"]="Rohan" # here we can change the data 
print(csv_1)
print('\n')

print(csv_1.loc[[2,3],["Name","Rank"]]) # get select row and col data
# if we want all row or all col data then we can use (:) instead of [2,3] or ["Name","Rank"]
print(csv_1.iloc[0,0]) # this is another method to get a particular data

print(csv_1.drop("Age",axis=1)) # to remove the full col of age(any col)
print(csv_1.drop(2,axis=0)) # to remove the full row of 2(any row)

# checking the pandas version
print('\n')
print("Pandas Version::-",pd.__version__)
print('\n')