# Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.

# Generate a random tuple
my_tuple = (1, 3, 5, 7, 8)

is_sorted = my_tuple == tuple(sorted(my_tuple))
print(is_sorted)