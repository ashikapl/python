# Problem Statement -> Using Decision-tree Model
'''You have been tasked with creating a decision tree model to predict whether a person is likely to purchase
a new smartphone based on their age, income and education level. You are provided with a dataset containing 
these attributes and the target variable indicating whether the person made a purchase or not.'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score
from sklearn.tree import DecisionTreeClassifier

# Here education level is define as 1->12th Pass, 2->bachelor's ,3->master's, 4->PHD, 5->Greater than PHD level
X = np.array([[30,40000,1],[40,100000,4],[34,30000,2],[50,200000,5],[25,20000,1],[5,90000,3]])
y = np.array([1,1,0,1,0,1]) # purchase 1 and not purchase 0

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print()
accuracy = accuracy_score(y_test, y_pred)
print("Model accuracy:-", accuracy)

# Take input from user
print()
user_age = int(input("Enter the customer age:- "))
user_salary = float(input("Enter the salary of customer:- "))
education_level = int(input("Enter the education level as(1->12th, 2->bachelor's, 3->Master's, 4->PHD, 5->Greater than PHD level):- "))

user_data = np.array([[user_age, user_salary, education_level]])
predication = model.predict(user_data)

if predication[0] == 1:
    print("The customer is likely to purchase.")
else:
    print("The customer is unlikely to purchase.")

print()