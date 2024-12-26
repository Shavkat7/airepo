# Get Unique Elements: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.

# Generate a random tuple
my_tuple = (1, 5, 7, 1, 3, 1, 8, 9, 1)

unique_tuple = tuple(dict.fromkeys(my_tuple))
print(unique_tuple)