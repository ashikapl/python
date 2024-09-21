# SubPlot in a single chat (multiple plots in one chat)
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([2,1,5,4])

# here 2,2 is row, col and 1 is index no.
plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("Data1")

a = np.array([6,7,8,9])
b = np.array([2,4,5,7])

plt.subplot(2,2,2)
plt.plot(a,b)
plt.title("Data2")

a = np.array([4,5,6,7])
b = np.array([3,4,5,6])

plt.subplot(2,2,3)
plt.plot(a,b)
plt.title("Data3")

a = np.array([1,2,3,4])
b = np.array([6,7,8,7])

plt.subplot(2,2,4)
plt.plot(a,b)
plt.title("Data4")

plt.suptitle("Data")
plt.show()