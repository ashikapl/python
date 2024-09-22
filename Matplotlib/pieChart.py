# Pie Chart
# As you can see the pie chart draws one piece (called a wedge) for each value in the array 
# By default the plotting of the first wedge starts from the x-axis and moves counterclockwise:

# The size of each wedge is determined by comparing the value with all the other values, by using this formula:
# The value divided by the sum of all values: x/sum(x)
import matplotlib.pyplot as plt
import numpy as np

x = np.array([56,88,67,76,89])
myLabels = ['Komal','Ram','Saloni','Vijay','Harsh']
myColor = ['green','hotpink','brown','darkblue','cyan']
# by default the angle is start from 0 we can change it by ourself also by startangle inbuilt function
plt.pie(x,labels=myLabels, radius=0.8, colors=myColor, startangle=20, shadow=True, explode=[0,0,0,0,0.1])
# this explode fuction cut the corresponding part at the no. of distance we are given
plt.legend(title='Percentage')
plt.show()

# there is some problem my chart is not showing in save file 

# # we can save our chart also in a file
# plt.savefig("pieChart.jpg", bbox_inches='tight', transparent=True)
# # or we can give location also and can also save in pdf
# plt.savefig("f:github/python/pieChart.pdf")