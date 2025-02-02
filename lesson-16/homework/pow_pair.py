# Task 2. Create a custom function that takes two arguments: a number and a power. 
# Use numpy.vectorize to calculate the power for each pair of numbers 
# in two arrays: [2, 3, 4, 5] and [1, 2, 3, 4].

import numpy as np

bases = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

def power(base, pow):
    return base**pow

vec_power = np.vectorize(power)

print(vec_power(bases, powers))