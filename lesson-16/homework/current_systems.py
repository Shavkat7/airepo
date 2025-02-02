# Given the electrical circuit equations below, solve for I1, I2, I3

import numpy as np

coef = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

b = np.array([12, -5, 15])

print(np.linalg.solve(coef, b))