# Problem Statement -> Using Logistic Regression
''' In an e-commerce company, the management want to predict whether a customer will purchase a high value product
based their age, time spent on the website and whether they have added items to their cart. The goal is to 
optimize marketing strategies by targeting potential customers  more effictively thereby increasing sales and revenue '''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = np.array([[20,30,0],[25,20,0],[30,50,1],[44,40,1]])
y = np.array([0,0,1,1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)

accuracy = model.score(X_test,y_test)
print("Model Accuracy:-", accuracy)

user_age = int(input("Enter the age of customer:- "))
user_timeSpent = float(input("Enter the time spent by the customer:- "))
user_addCart = int(input("Enter 1 if the customer add the product else 0:- "))

user_data = np.array([[user_age,user_timeSpent,user_addCart]])
prediction = model.predict(user_data)

if prediction[0] == 1:
    print("The customer is likely to purchase.")
else:
    print("The customer is unlikely to purchase.")