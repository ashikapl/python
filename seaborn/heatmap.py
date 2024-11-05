# Heatmap using seaborn 
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

var = np.linspace(1,15,20).reshape(4,5)
# print(var)

# sns.heatmap(var)
# plt.show()

data = sns.load_dataset("anagrams")
# print(data)
x = data.drop("attnr",axis=1).head(10) # here drop is used for removing (attnr) column which is string type
# print(x)
# sns.heatmap(x)

y = {"fontsize":20,"color":"g"}
var = np.linspace(1,10,10).reshape(2,5) 
# print(var)
v = sns.heatmap(var, vmin=0,vmax=10, cmap="PuOr",annot=True,annot_kws=y,
            linewidths=3,linecolor="black",cbar=False,xticklabels=False,yticklabels=False)
# xticklabels -> is to remove the x-axis points names
# yticklabels -> is to remove the y-axis points names
# cmap -> is for colour changing bars
# annot -> is showing the values on the bars
# cbar -> is to remove color bar from right side of the graph

# to set xlabel and ylabel you have to store the sns.heatmap into a variable
v.set(xlabel="Python",ylabel="Points")
sns.set(font_scale=20)

# var_1 = np.array([["a0","a1","a2","a3","a4"],
#                  ["b0","b1","b2","b3","b4"]])
# print(var_1)
plt.show()