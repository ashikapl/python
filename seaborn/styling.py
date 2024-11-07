# Styling plots 

import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
# print(data)

# can change figuare size
plt.figure(figsize=(5,20))

# can change size of names and number on the plot
sns.set_context("poster",font_scale=0.7) # paper and poster two ways to show the plot

sns.set_style("darkgrid") # darkgrid, whitegrid, white, dark
sns.barplot(x="day",y="tip",data=data,palette="cool") # hue="time" if error is showing use this
# plt.grid() 
# sns.despine() # which remove the axes which are at the top and left
plt.show()