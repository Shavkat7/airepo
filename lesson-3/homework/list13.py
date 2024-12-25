# Index of Element: Given a list and an element, find the index of the first occurrence of the element.

#generate any random list
my_list = [2, 3, 4, 15, "banana", 6, 6 ,32, "hello", 432, 2, 4, 15, "hello"]


try:
    element_to_find = input(f"Enter element you want to check presence in the list {my_list}: ")
    if element_to_find.isdigit(): #If input is integer
        element_to_find = int(element_to_find)
    elif element_to_find.replace(".", "", 1).isdigit() and element_to_find.count(".") == 1: #If input is float
        element_to_count = float(element_to_find)
    print(my_list.index(element_to_find))
except ValueError:
    print("No such value exists in the list!")