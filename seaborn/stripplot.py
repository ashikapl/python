# Stripplot :-> A strip plot is very simple to understand. It is basically a scatter plot that
# differentiate different categories. Strip plots are considered a good alternative to a box and violin plot.
import seaborn as sns
from matplotlib import pyplot as plt

data = sns.load_dataset("tips")
print(data)

sns.stripplot(x="day", y="total_bill", data=data, hue="sex", 
              palette="rocket_r",linewidth=1, edgecolor="yellow",
              jitter=0.2,size=7,marker="+",alpha=0.7)
#jitter -> split the dots in the graph

# sns.stripplot(x=data["total_bill"])
# plt.grid()
plt.show()