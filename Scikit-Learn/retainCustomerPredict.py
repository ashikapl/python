# Problem Statement -> Using Support Vector Machine
''' A telecommunication company wants to reduce customer churn(retain or not to leave) by identifying customers
at risk of leaving. They have historical data on customer behavoiur and want to build a model to predict which
customer are most likely to churn'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Churn Means -> The customer will recharge again or not 1 means leave and 0 means not leave
data = {"Age":[20,25,35,55,44,46,70,67], "MontlyRecharge":[20,40,50,60,70,35,55,80], "Churn":[0,0,0,1,1,0,0,1]}

df = pd.DataFrame(data)
# print(df)

X = df[["Age","MontlyRecharge"]]
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svm_model = SVC(kernel='linear',C=1.0) # default regularization
svm_model.fit(X_train,y_train)

y_pred = svm_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:-", accuracy)
print()
report = classification_report(y_test, y_pred)
print(report)
print()

user_age = int(input("Enter the age of the customer:- "))
user_montlyRechage = int(input("Enter the customer montly recharge:- "))

user_data = pd.DataFrame([[user_age, user_montlyRechage]], columns=["Age", "MontlyRecharge"])

prediction = svm_model.predict(user_data)

print()

if prediction[0] == 1:
    print("The customer are not likely to stay.")
else:
    print("The customer are likely to stay.")
    
print()
