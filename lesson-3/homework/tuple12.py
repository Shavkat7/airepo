# Find Second Largest: From a given tuple, find the second largest element.

# Generate a random tuple
my_tuple = (1, 5, 7, 8, 3, 10, -2, 12)

second_largest = sorted(set(my_tuple))[-2]
print(second_largest)