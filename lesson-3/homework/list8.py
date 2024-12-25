# Slice List: Create a new list that contains only the first three elements of the original list.

#generate any random list
my_list = [2, 3, 4, 15, "banana", 6, 6 ,32, "hello", 432, 2, 4, 15, "hello"]

if len(my_list) >= 3:
    new_list = my_list[:3]
    print(f"The new list containing first 3 elements of {my_list} is {new_list}")
else:
    print("The list contains less than 3 elements!")