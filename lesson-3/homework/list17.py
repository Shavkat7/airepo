# Concatenate Lists: Given two lists, create a new list that combines both lists.

#generate random lists
my_list = [2, 3, 4, 15, "banana", 6, 6 ,32, "hello", 432, 2, 4, 15, "hello"]
my_list2 = [85, 76, 9.89, 56, 23, 45, 56, -45]

my_list.extend(my_list2)
print(my_list)