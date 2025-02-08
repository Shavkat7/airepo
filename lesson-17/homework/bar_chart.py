# 7. Bar Chart
# Task: Create a vertical bar chart displaying the sales data 
# for five different products: ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']. 
# The sales values for each product are [200, 150, 250, 175, 225]. 
# Customize the chart with a title, axis labels, and different bar colors.

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['Product A', 'Product B', 'Product C', 'Product D', 'Product E'])
y = np.array([200, 150, 250, 175, 225])
z = np.array(['red', 'blue', 'green', 'm', 'indigo'])
plt.bar(x, y, color=z)
plt.title('Sales Data')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()