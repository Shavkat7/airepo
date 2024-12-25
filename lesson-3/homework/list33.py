# Find All Indices: Given a list and an element, find all the indices of that element in the list.

# generate random list
my_list = [2, 3, 4, 15, 6, 6, 32, 432, 2, 4, 15]

element_to_find = 15
indices = [i for i, x in enumerate(my_list) if x == element_to_find]
print(f"Indices of {element_to_find}: {indices}")
