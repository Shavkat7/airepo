# Find Maximum of Sublist: Given a list, find the maximum element of a specified sublist.

# generate random list
my_list = [2, 3, 4, 15, 6, 6, 32, 432, 2, 4, 15]

start, end = 2, 8  # example sublist indices
sublist = my_list[start:end]
print(f"The maximum of the sublist is: {max(sublist)}")
