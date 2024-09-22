# Histrogram Chart using python module (It is use for frequency distribution)
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(120, 10, 250)
y = np.random.normal(120, 10, 250)
plt.xlabel("BothGender")
plt.ylabel("Count")
plt.title("Population")
# there are more option in histtype
# or we can use orientation = vertical or horizontal
plt.hist([x,y], bins=4 ,rwidth=0.7, color=['g','b'], label=["Men", "Women"], histtype='bar', orientation='vertical') # bins means no. of parts
plt.legend()
plt.show()
