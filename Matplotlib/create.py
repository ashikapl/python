import matplotlib.pyplot as plt
import numpy as np

# plot (linear Graph)
x = np.array([1,2,3,4])
y = np.array([1,2,3,4])
plt.plot(x,y)
plt.show()
plt.plot(x,y,'o')
plt.show()

# bar Graph
c = ['r','y','b','g']
plt.bar(x,y,color = c)
plt.show()

# linear Graph
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()