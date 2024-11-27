# Problem Statement -> Using Random Forest 
'''Use a Random Forest Classifier to predict whether a person is likely to purchase a product based on their 
gender, and estimated Salary.'''

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Martial Status -> 1 means married and 0 means unmarried
# 'Marital_Status':[1,0,0,1,1,0,1,0,1,0],
data = {
      'Gender':['F','M','M','M','F','F','M','F','M','F'],
      'Salary':[20000,30000,45000,23000,60000,80000,91000,21000,33000,22000],
      'Purchased':[0,0,1,0,1,1,1,0,1,1]}

df = pd.DataFrame(data)
# print(df)

# Encoder Gender col in binary form
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
 
X = df.drop(['Purchased'], axis=1)
y = df['Purchased']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42) # n_estimators means 100 decision trees
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)

print()
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:-", accuracy)
print()     

# Take input from user
user_gender = input("Enter customer gender M/F:- ")
user_salary = int(input("Enter customer salary:- "))

user_gender_encoder = label_encoder.transform([user_gender])[0]

user_data = pd.DataFrame([[user_gender_encoder, user_salary]], columns=['Gender', 'Salary'])

prediction = rf_model.predict(user_data)

if prediction[0] == 1:
      print("The customer is likely to purchase.")
else:
      print("The customer is unlikely to purchase.")