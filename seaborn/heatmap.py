# Heatmap using seaborn 
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

var = np.linspace(1,15,20).reshape(4,5)
# print(var)

# sns.heatmap(var)
# plt.show()

data = sns.load_dataset("anagrams").head(10)
# print(data)
sns.heatmap(data)
plt.show()