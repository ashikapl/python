# Scatter Plot using seaborn
import seaborn as sns
from matplotlib import pyplot as plt

var = sns.load_dataset("penguins").head(40)
# print(var)

# sizes are between 1 to 100
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=var,hue="sex",style="sex",sizes=(100,50),
                palette="gist_ncar",markers={"Male":"^","Female":"*"},alpha=0.9)
plt.show()