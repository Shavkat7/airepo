import numpy as np

# Task 1. Write a Python function that converts a temperature from Fahrenheit to Celsius. 
# Use numpy.vectorize to apply this function to an array of temperatures: [32, 68, 100, 212, 77].

# Formula: 
# C=(F-32)*5/9

arr = np.array([32, 68, 100, 212, 77])

def far_to_cel(t):
    return (t-32)*5/9

vec_far_to_cel = np.vectorize(far_to_cel)

print((vec_far_to_cel(arr)).astype(int))