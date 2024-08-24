# Read in CSV file 

import pandas as pd

read_csv = pd.read_csv("F:\github\python\student.csv")
# print(read_csv)

# we can read only a selected row also
read_csv = pd.read_csv("F:\github\python\student.csv", nrows=3) # only starting 3 rows
# print(read_csv)

r = pd.read_csv("F:\github\python\student.csv", usecols=["Rank","Age"]) # here we can use 0,1,2 also instead of name
# print(r)

a = pd.read_csv("F:\github\python\student.csv", skiprows=[4]) # to skip full row from the data
# print(a) # prabhav data is skip here

i = pd.read_csv("F:\github\python\student.csv", index_col=2) 
# print(i) #  here col 2 is work as index of the data file

x = pd.read_csv("F:\github\python\student.csv", header=3)
# print(x) # here row 3 is work as header

y = pd.read_csv("F:\\github\\python\\student.csv", names=['col1','col2','col3','col4','col5'])
# print(y)

z = pd.read_csv("F:\\github\\python\\student.csv", header=None)
print(z) # here col value is come as 0,1,2,3,4

j = pd.read_csv("F:\\github\\python\\student.csv", dtype={"Marks":"float"})
# print(j)