# Scatter plot using python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x,y,color="hotpink",alpha=0.9)

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y,color='#88c999',alpha=0.7)
plt.show()

# we can use color list as same size of element in array of a and b
a = np.array([11,23,13,15,18,19,22])
b = np.array([99,86,87,88,111,86,110])
color = ['hotpink','cyan','pink','blue','lightgreen','yellow','brown']

plt.scatter(a,b,c=color)
plt.show()

# we can use colormap (viridis) or many more btwn (0-100) in numbers
p = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
q = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
color = [1,6,42,1,23,25,44,56,60,70,90,100,11]

plt.scatter(p,q, c=color, cmap="viridis")
# plt.scatter(p,q, c=color, cmap="Accent")
plt.colorbar()
plt.show()

i = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
j = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = [1,6,42,1,23,25,44,56,60,70,90,100,11]

plt.scatter(p,q, s=sizes)
plt.show()

d = np.random.randint(100, size=(50))
f = np.random.randint(100, size=(50))
colors = np.random.randint(100, size=(50))
sizes = 10 * np.random.randint(100, size=(50))

plt.scatter(d, f, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()