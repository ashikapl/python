# Problem statement -> Using Gradient-Boosting Model(algo)
'''Create a predictive model using Gradient Boosting to forcast housing prices based on various features such
as square footage, number of bedrooms, number of bathrooms and location.'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

data = {'Square_Foot':[1500,2000,2500,1850,3000],
        'Bedrooms':[1,2,3,2,4],
        'Bathrooms':[1,2,2,1,2],
        'Location':['Suburb','City','Rural','City','Suburb'],
        'Prices':[100000,200000,300000,185000,400000]}

df = pd.DataFrame(data)
# print(df)

# Convert the location column dummy
df = pd.get_dummies(df, columns=['Location'])
# print(df)

X = df.drop('Prices', axis=1)
y = df['Prices']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GradientBoostingRegressor()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
print("Mean-Square-error:-", mse)

print()
print("--Enter the detail for house price predictions--")
sq_footage = float(input("Enter the square footage:- "))
bedroom = int(input("Enter the number of bedrooms required:- "))
bathroom = int(input("Enter the number of bathrooms:- "))
location = input("Enter the location (Suburb/City/Rural):- ")

input_location = [0,0,0]

if location == 'Suburb':
    input_location[0] = 1
elif location == 'City':
    input_location[1] = 1
elif location == 'Rural':
    input_location[2] = 1
    

user_data = pd.DataFrame({'Square_Foot':[sq_footage],
                          'Bedrooms': [bedroom],
                          'Bathrooms': [bathroom],
                          'Location_City': [input_location[1]],
                          'Location_Rural':[input_location[2]],
                          'Location_Suburb':[input_location[0]]})

prediction = model.predict(user_data)
print()
print(f"The price of house is: {prediction}")
print()