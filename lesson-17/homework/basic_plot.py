import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 11)
y= x ** 2 - 4 * x + 4

plt.scatter(x, y, c=x, cmap="cool")
plt.colorbar()
plt.title("Hello, this is first task")
plt.xlabel("This is X label")
plt.ylabel("This is Y label")
plt.show()