# Boxplot --> it show the median value as box shape and min and max value int line as whisker plot
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
# print(data)

# sns.boxplot(x="day",y="total_bill",data=data,hue="sex",palette="magma",
#             linewidth=2,linecolor="brown",gap=0.2,saturation=0.9,
#             order=["Sun","Thur","Fri","Sat"],showmeans=True,
#             meanprops={"marker":"*","markeredgecolor":"black"})
# Saturation is boxs color density

# sns.set(style="whitegrid") # we can create grid also in boxplot
sns.boxplot(data=data,orient="h") # orient -> horizontal, vertical
# sns.boxplot(x=data["tip"]) 
plt.show()