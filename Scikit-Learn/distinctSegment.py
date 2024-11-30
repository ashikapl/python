# Problem Statement -> Using Gaussion Mixture Models (GMM)
'''As a retail business owner you want to understand and categorize your customers into distinct 
segments based on their purchasing behaviour. This segmentation will help you tailor marketing
strategies and promotion of different customer groups, ultimately maximizing sales and customer
and customer satisfaction.'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture

np.random.seed(42)
segment1 = np.random.normal(loc=30,scale=5,size=100)
segment2 = np.random.normal(loc=60,scale=10,size=150)
segment3 = np.random.normal(loc=90,scale=8,size=120)

data = np.concatenate([segment1,segment1,segment3]).reshape(-1,1)

scaler = StandardScaler()
scaler_data = scaler.fit_transform(data)

n_comp = 3
gmm = GaussianMixture(n_components=n_comp, random_state=42)
gmm.fit(scaler_data)

cluster_labels = gmm.predict(scaler_data)

# Draw plot
plt.scatter(data, np.zeros_like(data), c=cluster_labels, cmap='viridis')
plt.title('Cluster Segmentation')
plt.xlabel('Purchase Amount')
plt.show()

# User input
user_input = float(input("Enter a purchase amount to predict the customer segement:- "))
user_input_scaled = scaler.transform(np.array([[user_input]]))
prediction = gmm.predict(user_input_scaled.reshape(-1,1))[0]

print(f"The predicted customer segment for a purchase amount of {user_input_scaled} is: {prediction}")