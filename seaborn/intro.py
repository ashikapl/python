# Seaborn Module Intro similar as matplotlib but better to work with large data set 
# lineplot in seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

var = [1,2,3,4,5,6,7]
var_1 = [3,2,5,4,1,6,7]

x_1 = pd.DataFrame({"var":var, "var_1":var_1})

y_1 = sns.load_dataset("penguins").head(30)
# print(y_1)
# sns.lineplot(x="var",y="var_1",data=x_1)
# sns.lineplot(x="bill_length_mm",y="bill_depth_mm",data=y_1)
sns.lineplot(x="bill_length_mm",y="bill_depth_mm",data=y_1, hue="sex",
             style="sex",markers=["o","*"],palette="deep",dashes=False,legend="full")
# palette is for color changing 
# dashes remove all dotted line and print plane line 
plt.grid()
plt.title("Seaborn",size=25)
plt.show()
