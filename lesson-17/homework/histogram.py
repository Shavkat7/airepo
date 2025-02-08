# Histogram
# Task: Generate a random dataset of 1000 values sampled from a normal distribution (mean=0, std=1). 
# Plot a histogram of the data with 30 bins. Add a title and axis labels. 
# Adjust the transparency of the bars using the alpha parameter.

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 1, 1000)


plt.hist(x, bins=30, alpha=0.7)
plt.title("This is Histogram")
plt.xlabel("X LABEL")
plt.ylabel("Y LABEL")
plt.show()