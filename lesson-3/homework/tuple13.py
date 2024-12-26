# Find Second Smallest: From a given tuple, find the second smallest element.

# Generate a random tuple
my_tuple = (1, 5, 7, 8, 3, 10, -2, 12)

second_smallest = sorted(set(my_tuple))[1]
print(second_smallest)