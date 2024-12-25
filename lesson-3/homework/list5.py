# Check Element: Given a list and an element, check if the element is present in the list.

#generate any random list
my_list = [2, 3, 4, 15, "banana", 6, 6 ,32, "hello", 432, 2, 4, 15, "hello"]

try:
    element_to_contain = input(f"Enter element you want to check presence in the list {my_list}: ")
    if element_to_contain.isdigit(): #If input is integer
        element_to_contain = int(element_to_contain)
    elif element_to_contain.replace(".", "", 1).isdigit() and element_to_contain.count(".") == 1: #If input is float
        element_to_count = float(element_to_contain)
    print(my_list.__contains__(element_to_contain))
except:
    print("Error occured!")