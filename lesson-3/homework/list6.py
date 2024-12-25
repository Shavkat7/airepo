# First Element: Access the first element of a list, considering what to return if the list is empty.

#generate any random list
my_list = [2, 3, 4, 15, "banana", 6, 6 ,32, "hello", 432, 2, 4, 15, "hello"]

try:
    print(f"First element in the list {my_list} is {my_list[0]}")
except IndexError:
    print("The list is empty!")