# Substitution Method By Data Visualization Module Matplotlib
# Linear Algebra
import matplotlib.pyplot as plt
import numpy as np

# Eqn 1
# y = 3x
# -5x + 2y = 2

x = np.linspace(-10,10,1000) # start, end, npoints
y1 = 3 * x
y2 = (2 + 5*x)/2

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim([0,3])
plt.ylim([0,8])
plt.plot(x,y1,color="brown")
plt.plot(x,y2,color="green")
plt.axvline(x=2,color="purple",linestyle="--")
plt.axhline(y=6,color="purple",linestyle="--")
plt.show()

# 2x - 3y = 15
# 4x + 10y = 14

y3 = -5 + (2*x/3)
y4 = (7-2*x)/5

plt.axvline(x=0, color="lightgray")
plt.axhline(y=0, color="lightgray")

plt.xlim([-2,10])
plt.ylim([-6,4])
plt.plot(x,y3,c="blue")
plt.plot(x,y4,c="pink")
plt.axvline(x=6,color="purple",linestyle="--")
plt.axhline(y=-1,color="purple",linestyle="--")
plt.show()