# Problem Statement -> Using Neural Network
'''You are tasked with creating a neural newtwork model to predict whether a student will pass or fail an exam 
based on two features: hours student and previous exam scores. The dataset should contains information on
studied and previous exam scores for a group of students, along with their exam outcomes (Pass or Fail)'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder

study_hours = [1.5,2.0,5.5,6.0,3.5,8.0]
prev_exam_scores = [50,55,67,70,60,80]
exam_outcome = ['Fail','Fail','Pass','Pass','Fail','Pass']

# Transform the string in Binary 
label_encoder = LabelEncoder()
encoded_exam_outcome = label_encoder.fit_transform(exam_outcome)

# Combine the array to form a DataFrame or Matrix
X = np.column_stack((study_hours, prev_exam_scores))
y = encoded_exam_outcome

classifier_model = MLPClassifier(hidden_layer_sizes=(4,), activation='logistic', max_iter=5000, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
classifier_model.fit(X_train,y_train)

new_student_data = np.array([[5.5,60]])

prediction = classifier_model.predict(new_student_data)

prediction_decode = label_encoder.inverse_transform(prediction)

print(F"The exam outcome of student is: {prediction_decode[0]}")

