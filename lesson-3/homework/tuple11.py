# Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.

# Generate a random tuple
my_tuple = (1, 5, 7, 1, 3, 1, 8, 9, 1)
element = 1

indices = [i for i, x in enumerate(my_tuple) if x == element]
print(indices)