import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

x = np.linspace(-5, 5, 10000)
x_log = np.linspace(0, 10, 400)

y1 = x**3
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(x_log + 1)

plt.figure(figsize=(10, 3))


plt.subplot(2, 2, 1)
plt.plot(x, y1, color='red', marker='')
plt.title("$ f(x) = x^3 $")
# plt.show()

plt.subplot(2, 2, 2)
plt.plot(x, y2, color='green')
plt.title("$ f(x) = \sin(x) $")
# plt.show()

plt.subplot(2, 2, 3)
plt.plot(x, y3, color='black')
plt.title("$ f(x) = e^x $")
# plt.show()

plt.subplot(2, 2, 4)
plt.plot(x_log, y4, color='yellow')
plt.title("$ f(x) = \log(x+1) $ (for $ x \geq 0 $)")
plt.show()