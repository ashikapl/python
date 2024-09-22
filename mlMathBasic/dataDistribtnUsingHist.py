# To create big data sets for testing, we use the Python 
# module NumPy, which comes with a number of methods to create random data sets, of any size.

# Data Distribution using Histrogram for easy understanding and work with big data
import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(0.0, 0.4, 120) # here 0.0 is starting no. upto 0.4 system can choose random no
# we can create a histogram for easy to understand the data
plt.hist(x, 20, rwidth=0.9) # here 20 is bars(boxes)
plt.show()