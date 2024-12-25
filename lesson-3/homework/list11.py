# Remove Duplicates: Given a list, create a new list that contains only unique elements from the original list.

#generate any random list
my_list = [2, 3, 4, 15, "banana", 6, 6 ,32, "hello", 432, 2, 4, 15, "hello"]

new_list = list(set(my_list))
print(f"Unique elements in the list {my_list}\n are {new_list}")