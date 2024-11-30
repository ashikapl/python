# Problem Statement -> Using DBSCAN (Density based spatial clustering of application with the noise.)
'''Imagine you are working for an e-commerce company, and the marketing team wants to target customers
more efficently by creating segments based on their purchasing behaviour. However, traditional
segmentation methods are not providing satisfactory results.'''
# To identify clusters of customers with similar purchasing patters.

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.random.rand(100,2) # 100 points with 2 features

scaler = StandardScaler()
scaler_data = scaler.fit_transform(data)

dbscan = DBSCAN(eps=0.3,min_samples=5) # eps -> Maximum distance btwn two samples
clusters = dbscan.fit_predict(scaler_data)
 
# Draw Plot
plt.scatter(data[:,0], data[:,1], c=clusters, cmap='rainbow', marker='o',s=50)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('DBSCAN Clustering')
plt.show()

result_df = pd.DataFrame({'Feature1':data[:,0],
                          'Feature2':data[:,1],
                          'Cluster':clusters})

print('Number of clusters:',len(np.unique(clusters)))
print('Size of each cluster:')
print(result_df['Cluster'].value_counts)

# Input User
user_input = np.array([[0.1,0.3]])
user_input_scaled = scaler.transform(user_input)
predict_cluster = dbscan.fit_predict(user_input_scaled)
print("User input belongs to cluster:", predict_cluster[0])