# FacetGrid ->>> function with the help of which we can create multiple plot in a single sheet
import seaborn as sns
import matplotlib.pyplot as plt

var = sns.load_dataset("tips")
# print(var)

# FacetGrid using seaborn and matplotlib map function
# col -> differentiate into two col plots female and male in which (day) is differentiate in both the plots
fg = sns.FacetGrid(var,col="sex",hue="day",palette="cool")
fg.map(plt.bar,"total_bill","tip",edgecolor="black").add_legend()
plt.show()

# FacetGrid using seaborn map+dataFrame
g = sns.FacetGrid(var, col="time", hue="sex")
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.add_legend()
plt.show()
