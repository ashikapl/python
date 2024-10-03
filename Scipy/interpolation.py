# Interpolation refers to the process of estimating values between known data points. 
# It is commonly used to predict or fill in values where data may be missing or
# when a smooth transition between discrete points is required.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(11)
y = np.array([2.0,3.0,1.5,5.5,0.9,0.1,0.5,2.9,6.0,7.6,2.2])

# plt.plot(x,y,"o:")
# plt.show()

from scipy.interpolate import interp1d
# 'linear', 'quadratic', 'cubic', 'nearest', 'zero', 'slinear'
predict = interp1d(x,y,kind='linear')

x1 = np.linspace(0,10,100)
y1 = np.array([predict(i) for i in x1])

plt.plot(x,y,"o:")
plt.plot(x1,y1,"ro:")
plt.show()

print("x: (1.5)y:-", predict(1.5))