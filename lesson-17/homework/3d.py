#  3D Plotting
# Task: Create a 3D surface plot for the function $ f(x, y) = \cos(x^2 + y^2) $ 
# over the range of $ x $ and $ y $ values from -5 to 5. 
# Use a suitable colormap and add a colorbar. 
# Set appropriate labels for the axes and title.

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = plt.axes(projection='3d')


x = np.random.randint(-10000, 10000, 100)
y = np.random.randint(-10000, 10000, 100)

xx, yy = np.meshgrid(x, y)

z = np.cos(xx ** 2 + yy ** 2)

ax.plot_surface(xx, yy, z, cmap='viridis')
plt.show()