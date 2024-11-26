# Predict the student's final exam score based on the number of hours they study -> Using Linear Regression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split # its for split the data into two parts training and test
from sklearn.linear_model import LinearRegression # for continues data prediction

# Step1 -> Create a dataset(DataFrame) or load using pandas or sklearn
data = {'Study_Hours':[1,2,4,5,6,8,9,10], 
        'Scores':[50,55,65,70,75,80,88,92]}
# print(data)

df = pd.DataFrame(data)
# print(df)

# Step3 -> Feature and target
X = df[['Study_Hours']]
y = df['Scores']

# Step3 -> Split the data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Random state pending topic

model = LinearRegression()
model.fit(X_train,y_train)

#  Step4 -> Take input form user to predict the score
print()
user_input = float(input("Enter the Study_Hours:- "))
user_input_df = pd.DataFrame([[user_input]], columns=["Study_Hours"])

# Step5 -> Predict function for user input prediction
model_pred = model.predict(user_input_df)

# Step6 -> Print the predicted scores
print(f"Predicted Exam Score:- {model_pred[0]:.2f}") # [0] for first index and 2f is 2 decimal number after point
print()