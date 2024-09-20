# more functions use in linear graph
import matplotlib.pyplot as plt
import numpy as np

days = np.array([1,2,3,4,5,6,7])
min = np.array([67,66,60,65,77,88,67])
max = np.array([44,55,45,56,65,67,70])
avg = np.array([33,23,25,26,28,29,32])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.xlabel("Days", font2)
plt.ylabel("Temperature", font2)
plt.title("Weather", font1, loc = 'center')

plt.plot(days, max, label="Max")
plt.plot(days, avg, label="Avg")
plt.plot(days, min, label="Min")

plt.legend(loc="best", shadow=True, fontsize="large") 
# here we can use in loc function parameter = upper right, upper left, bottom right, 
# bottom left but best will automatically adjust its space
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5, axis='x') #and also use axis = x or y or both
plt.show()