# Repeat Elements: Given a tuple and a number, create a new tuple where each element is repeated that number of times.

# Generate a random tuple
my_tuple = (1, 5, 7)

repeated_tuple = tuple(x for x in my_tuple for _ in range(3))
print(repeated_tuple)