# Min Element: From a given list, determine the smallest element.

#generate any random list
my_list = [85, 76, 9.89, 56, 23, 45, 56, -45]

try:
    print(f"Minimum of all the elements in the list {my_list} is {min(my_list)}")
except ValueError as e:
    print(f"The list is empty: {e}")