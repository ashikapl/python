# Countplot ->> countplot plots the count of the number of records by category
# Barplot ->> Barplot plots a value or metric for each category (by default, barplot the mean of a variable, by category)
import seaborn as sns
from matplotlib import pyplot as plt

var = sns.load_dataset("tips")
# print(var)
sns.countplot(x="sex", data=var, hue="smoker", palette="bwr",saturation=0.6)
# saturation is for color bars visualization(light or Dark)
# Here we can use (color) parameter also in place of (palette) to change the colour

# sns.countplot(y="sex", data=var)
plt.show()

# Barplot
sns.barplot(x="sex",y="size",data=var)
plt.show()