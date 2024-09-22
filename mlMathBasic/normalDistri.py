# Normal data distribution using python module 
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(6.0, 1.0, 1000) 
# here 1.0 is standard deviation, 5.0 is mean value and 1000 is no of random value under

plt.hist(data, 100)
plt.show()