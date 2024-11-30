# Problem Statement -> Using Agglomerative Hierarichical Clustering
'''You are the data scientist at a retail company and the marketing team is looking to optimize their promotional
campaigns segments. The goal is to identify distinct groups of customers based on their demographic information
such as age, income and spending score.'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import cdist

np.random.seed(42)
df = pd.DataFrame({'Age':np.random.randint(18,90,100),
                     'Income':np.random.randint(30000,100000,100),
                     'SpendingScore':np.random.randint(1,100,100)})

scaler = StandardScaler()
scaler_data = scaler.fit_transform(df)

clustering_model = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
df['Cluster'] = clustering_model.fit_predict(scaler_data)
# print(df)

# Compute cluster centroids
centroids = df.groupby('Cluster').mean()

# Draw a plot
plt.scatter(df['Income'], df['SpendingScore'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Income')
plt.ylabel('SpendingScore')
plt.title('Income and SpendingScore plot')
plt.show()

# input from user
user_data = pd.DataFrame({'Age':[30000],
                          'Income':[50],
                          'SpendingScore':[20]})

scaler_user_data = scaler.transform(user_data)

# Find the closest cluster for user data
centroids_scaled = scaler.transform(centroids)  # Scale centroids for comparison
distances = cdist(scaler_user_data, centroids_scaled)  # Calculate distances to centroids
closest_cluster = np.argmin(distances)  # Find the closest cluster

print()
print(f"The customer belongs to: {closest_cluster}")
print()