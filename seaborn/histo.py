# Histogram using seaborn
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Here (displot) function is used to create Histogram

data = sns.load_dataset("penguins")
# print(data)
sns.displot(data["flipper_length_mm"],color="green",kde=True,rug=True,log_scale=False)
# kde -> Kernel Density Estimate which is a plane line at top of histogram
# rug -> a function that shows the distribution of individual data points along an axis by drawing ticks along the x and y axes
# log_scale -> is for showing the graph in log values if log_scale is true and if false then no change the x-axis is showing normal values
sns.displot(data["flipper_length_mm"],bins=[170,180,190,200,210,220,230,240],color="brown")
plt.show()
