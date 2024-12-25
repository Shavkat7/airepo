# Max Element: From a given list, determine the largest element.

#generate any random list
my_list = [85, 76, 9.89, 56, 23, 45, 56, -45]

try:
    print(f"Maximum of all the elements in the list {my_list} is {max(my_list)}")
except ValueError as e:
    print(f"The list is empty: {e}")