# 1. Return uncommon elements of lists. Order of elements does not matter.

#generate any random lists
my_list = [2, 3, 4, 15, "banana", 6, 6 ,32, "hello", 432, 2, 4, 15, "hello"]
my_list2 = [85, 76, 9.89, 56, 23, 45, 56, -45, 432]

unique_list = []
for el in my_list:
    if el not in my_list2:
        unique_list.append(el)
for i in my_list2:
    if i not in my_list:
        unique_list.append(i)

print(unique_list)