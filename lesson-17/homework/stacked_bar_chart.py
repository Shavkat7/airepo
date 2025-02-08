#  Stacked Bar Chart
# Task: Create a stacked bar chart that shows 
# the contribution of three different categories ('Category A', 'Category B', and 'Category C') 
# over four time periods ('T1', 'T2', 'T3', 'T4'). 
# Use sample data for each category at each time period. 
# Customize the chart with a title, axis labels, and a legend.

import matplotlib.pyplot as plt
import numpy as np

time_periods = ['T1', 'T2', 'T3', 'T4']
category_a = np.array([10, 20, 30, 40])
category_b = np.array([20, 15, 25, 35])
category_c = np.array([30, 25, 20, 15])

plt.bar(time_periods, category_a, label='Category A', color='skyblue')
plt.bar(time_periods, category_b, label='Category B', color='orange', bottom=category_a)
plt.bar(time_periods, category_c, label='Category C', color='green', bottom=category_a + category_b)

plt.title('Contribution of Categories Over Time')
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.legend(title='Categories')

plt.show()
