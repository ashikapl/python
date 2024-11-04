# Barplot using seaborn 
import seaborn as sns
# import pandas as pd
from matplotlib import pyplot as plt

var = sns.load_dataset("penguins")
# print(var)
# two types to show a bar graph
# sns.barplot(x=var.island,y=var.bill_depth_mm)
sns.set(style="darkgrid")
order_1 = ["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y="bill_depth_mm",data=var,hue="sex",
            order=order_1,hue_order=["Male",'Female'], errorbar=('ci', 50), 
            palette="dark:g",saturation=50,err_kws={'color':'y','linewidth':5},dodge=True)
# dodge is for mixing the both bars of male and female at same point
# alpha=0.4 is for graph blurness 
# staturation is for the line at the top of bars blurness
# capsize=0.5 is a parameter for line the top and down of the confidence intervals line
# sns.barplot(x="bill_length_mm", y="bill_depth_mm",data=var,orient='h') # Here h means horizontal
# confidence intervals for (ci) height of the line top of the bars
# here (hue) parameter is for differentiating two or more values
plt.show()
