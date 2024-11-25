# House Price Prediction 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("F:\github\python\Scikit-Learn\housePrice.csv")
print(data)

plt.xlabel("Area")
plt.ylabel("Price")
plt.title("House Price Predict")
plt.scatter(data.area,data.price,marker='+',color='Black')
plt.show()

X = data[['area']]
y = data['price']

model = LinearRegression()
model.fit(X,y)

predict_price = model.predict(X)

feature_names = 'area'
target_names = 'price'

print()
print("Feature-Names:-",feature_names)
print("Target-Names:-",target_names)
print()

sample1 = [[2000,3000,4000,5000,6000]]
# Plotting predictions (Optional)
plt.scatter(data['area'], data['price'], marker='+', color='Black')
plt.plot(data['area'], predict_price, color='Blue')  # Line of best fit
plt.scatter(sample1,data['price'])
plt.plot(data['area'], predict_price)
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("House Price Prediction with Linear Regression")
plt.show()