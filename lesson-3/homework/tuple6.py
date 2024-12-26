# Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.

# Generate a random tuple
my_tuple = (1, 5, 7, 8)

last_element = my_tuple[-1] if my_tuple else None
print(last_element)