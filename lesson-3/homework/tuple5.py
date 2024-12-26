# First Element: Access the first element of a tuple, considering what to return if the tuple is empty.

# Generate a random tuple
my_tuple = (1, 5, 7, 8)

first_element = my_tuple[0] if my_tuple else None
print(first_element)