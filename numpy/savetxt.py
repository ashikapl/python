# Save txt of numpy array in a file
import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9]])

np.savetxt("savetxt",x)