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

plt.plot(xpoints, ypoints, 'r:o', ms = 10, mec = 'r', mfc = 'b', alpha = 0.5) 
# there are many more function instead of r:o 
# here (r) means red (:) means dot line and (+) means plus sign at the mid points This is a format function we can use in plot parameter
# There is markersize(ms), markerFaceColor(mfc) and markerEdgeColor(mec) functions to set the size,markercolor, and their edge colors
# one more imp function is (alpha) to for strong or weak visualization  btwn (0-1)
plt.show()