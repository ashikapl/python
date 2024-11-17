# Pizza Prices Prediction using (Linear Regression)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step1 :- Firstly create the dataset using Pandas(Data Collection)
pizzaPrice = {'Diameter':[2,4,6,8,10,12,11,15,17], 'Prices':[10,13,15,17,20,21,25,28,30]}

df = pd.DataFrame(pizzaPrice)
# print(df)

# Step2 :- Calculate 
# Y = mX + b (Here Y is dependent variable, X is independent variable, m is slope of the line and b is intercept point)
X = df['Diameter']
Y = df['Prices']

# find mean x and y
mean_x = np.mean(X)
mean_y = np.mean(Y)

print(f"Mean of X:- {mean_x}")
print(f"Mean of Y:- {mean_y}")

# Calculate slope(m) and intercept(b) values
# m = sum of product of devitaion / sum of square of deviation of X
num = np.sum((X - mean_x) * (Y - mean_y))
deno = np.sum((X-mean_x) ** 2)
m = num / deno

# b = Y-(mX) ==> intercept(B) = mean(Y) - M*mean(X)
b = mean_y - m * mean_x

print(f"Slope m:- {m}")
print(f"Intercept b:- {b}")

# Step3 :- Find the Y(price)
df['predictPrices'] = m * df['Diameter'] + b

# Step4 :- Visualize the Data
plt.plot(X, Y, marker='o', c="violet")

plt.title("Pizza Price Prediction")
plt.xlabel("Diameter of Pizza")
plt.ylabel("Prices of Pizza")
plt.show()
