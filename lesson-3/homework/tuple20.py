# Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.

# Generate a random tuple
my_tuple = (1, 5, 7, 8, 3, 10)

nested_tuple = ((my_tuple[0], my_tuple[1]), (my_tuple[2], my_tuple[3]))
print(nested_tuple)