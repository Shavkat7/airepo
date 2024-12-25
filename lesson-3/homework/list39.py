# Create Nested List: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.

# generate random list
my_list = [2, 3, 4, 15, 6, 6, 32, 432, 2, 4, 15]

n = 3  # number of elements in each sublist
nested_list = [my_list[i:i + n] for i in range(0, len(my_list), n)]
print(nested_list)
