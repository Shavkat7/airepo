# Task 3. Solve the system of equations using numpy:

# 4*x+5*y+6*z=7
# 3*x-y+z=4
# 2*x+y-2*z=5

import numpy as np

A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

b = np.array([7, 4, 5])

print(np.linalg.solve(A, b).round(2))