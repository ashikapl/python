# Create a CSV file 

import pandas as pd

dist = {'A':[11,12,13,14,15],'B':[10,20,30,40,50],'C':[90,80,70,60,50]}

d = pd.DataFrame(dist)
# d.to_csv("Test.csv")
d.to_csv("example.csv", index=False, header=[1,2,3])

# create a file for using to read the data in other readCSV.py name file
student_data = {'Name':['Mohit','Rohit','Raghav','Prabhav','Tanay'],'Age':[12,14,11,10,16],'Suject':['Bio','Maths','Commerce','Acts','Science'],'Marks':[66,88,57,89,91],'Rank':[4,3,5,2,1]}
s = pd.DataFrame(student_data)
s.to_csv("Student.csv", index = False)

MissData = {'Name':['Nikhil','Kamlesh','Mohan','Deepak','Hitesh','NaN','Harish'],
            'Branch':['COE','COE','IT','MCE','NaN','NaN','NaN'],
            'Year':['2022','NaN','2012','2021','2024','NaN','2024'],
            'CGPA':['9.7','9.1','9.4','9.5','9.0','NaN','9.2',]}
m = pd.DataFrame(MissData)
m.to_csv("MissData.csv", index=False)
print(m)