# Find Second Smallest: From a given list, find the second smallest element.

# generate random list
my_list = [2, 3, 4, 15, "banana", 6, 6, 32, "hello", 432, 2, 4, 15, "hello"]

my_list = list(filter(lambda x: type(x) == int or type(x) == float, my_list))
my_list.sort()
try:
    print(my_list[1])  # second smallest element
except IndexError:
    print(f"Index is not consistent with length of {my_list}")
