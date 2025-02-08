# 4. Scatter Plot
# Task: Create a scatter plot of 100 random points in a 2D space. 
# The x and y values should be randomly generated from a uniform distribution between 0 and 10. 
# Use different colors and markers for the points. Add a title, axis labels, and a grid.

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0, 10, 100)
y = np.random.randint(0, 10, 100)

plt.scatter(x, y, c=y)
plt.colorbar()
plt.grid(alpha=0.2)
plt.title("Random scatterplot")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()