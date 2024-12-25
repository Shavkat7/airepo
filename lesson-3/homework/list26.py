# Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.

# generate random list
my_list = [2, 3, 4, 15, "banana", 6, 6, 32, "hello", 432, 2, 4, 15]

mid_index = len(my_list) // 2
if len(my_list) % 2 == 0:
    print(my_list[mid_index - 1], my_list[mid_index])  # two middle elements
else:
    print(my_list[mid_index])  # one middle element
