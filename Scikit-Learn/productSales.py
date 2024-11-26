# Problem statement -> Using KNN (K-Nearest-Neighbors) algo
'''A retail company want to predict customer purchasing behaviour based on their age, salary and past purchase 
history. The company aims to use KNN(K-Nearest-Neighbors) algo to classify customers into potential buying
groups to personalize marketing strategies. This predictive model will help the company understand and target
specific customer segments more effectively, thereby increasing sales and customer satisfaction.'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

data = np.array([[25,30000,2],[30,40000,1],[55,60000,1],[20,35000,2],[50,50000,3],[45,25000,3],[60,90000,2]])
target = np.array([1,0,0,1,2,2,1]) # 0 Low, 1 Medium, and 2 High

X_train, X_test, y_train, y_test  = train_test_split(data, target, test_size=0.2, random_state=42)

# This StandardScaler function sort the data in correct manner
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)

print()
accuracy = knn.score(X_test, y_test)
print("Knn Accuracy:-", accuracy)

user_age = int(input("Enter the age of customer:- "))
user_salary = float(input("Enter the salary of customer:- "))
user_productBuy = int(input("Enter the product customer buys:- "))

user_data = np.array([[user_age, user_salary, user_productBuy]])
user_data_scaled = scaler.transform(user_data) 

prediction = knn.predict(user_data)

if prediction[0] == 0:
    print("Predicted buying group: Low")
elif prediction[0] == 1:
    print("Predicted buying group: Medium")
else:
    print("Predicted buying group: High")

# Explore more in this concept 
