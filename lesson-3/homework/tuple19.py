# Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.

# Generate a random tuple
my_tuple = (1, 5, 7, 8, 3, 10)

element_to_remove = 7
new_tuple = tuple(x for x in my_tuple if x != element_to_remove or (element_to_remove := False))
print(new_tuple)