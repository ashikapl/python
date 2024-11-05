# Distribute the data a each point like a box and whisker plot and make bars in violin shape like structure
import seaborn as sns
from matplotlib import pyplot as plt

data = sns.load_dataset("tips").head(200)
# print(data)

sns.violinplot(x="day",y="total_bill",data=data,hue="smoker",palette="light:orange",linewidth=1,saturation=0.4)
# sns.violinplot(x="day",y="total_bill",data=data,hue="sex",split=True,density_norm="count")
# we can create it in horizontal form to change x parameter into y and y parameter into x parameter
# density_norm -> count means the male and female total_bill ke according the violin change its shape

# sns.violinplot(x="sex",y="total_bill",data=data,order=["Male","Female"], inner="points")
# inner -> is for changing the inner plots into -> box,points,stick,none,quartile
# sns.violinplot(x="time",y="total_bill",data=data,order=["Dinner","Lunch"])

# we can create single violin plot only on numerical data
# sns.violinplot(x=data["size"])

plt.show()