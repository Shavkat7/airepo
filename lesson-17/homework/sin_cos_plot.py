import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.arange(0, 2*np.pi, 0.001)
cos = np.cos(x)
sin = np.sin(x)

plt.plot(x, cos, label="cos(x)", linestyle="--", marker="+")
plt.plot(x, sin, label="sin(x)", linestyle="-.", marker='8')

plt.legend()
plt.show()