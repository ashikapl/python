# Problem Statement -> Using K-Means Clustering
'''A mall wants to understand its customer base better to improve its marketing strategy. The goal it to cluser
customers into groups based on their annual income and spending score, so the marketing team can tailor their 
campaigns to each clusters preferences and behaviour.'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

np.random.seed(42)
data = {'Annual_Income':np.random.randint(30000,100000,100), 'Spending_Score':np.random.randint(1,100,100)}
df = pd.DataFrame(data)
# print(df)

# Draw graph
plt.scatter(df['Annual_Income'], df['Spending_Score'])
plt.title('Customer Data Annual_Income Vs Spending_Score')
plt.xlabel('Annual_Income')
plt.ylabel('Spending_Score')
plt.show()

X = df.values
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)
# print(df)

# Clusters Graph
plt.scatter(df['Annual_Income'], df['Spending_Score'], c=df['Cluster'],cmap='rainbow')
plt.title('kMeans Clustering Annual_Income Vs Spending_Score')
plt.xlabel('Annual_Income')
plt.ylabel('Spending_Score')
plt.show()

# Input from user
user_input = {'Annual_Income':[75000], 'Spending_Score':[70]}
user_df = pd.DataFrame(user_input)

user_array = user_df.values
prediction = kmeans.predict(user_array)

print(f"The customer belongs to: {prediction[0]}")

print()
print(df.head())
print()

