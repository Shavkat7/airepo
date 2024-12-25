# Count Occurrences: Given a list and an element, find how many times the element appears in the list.

#generate any random list
my_list = [2, 3, 4, 15, "banana", 6, 6 ,32, "hello", 432, 2, 4, 15, "hello"]

try:
    element_to_count = input("Enter element to count: ")
    if element_to_count.isdigit(): #If input is integer
        element_to_count = int(element_to_count)
    elif element_to_count.replace(".", "", 1).isdigit() and element_to_count.count(".") == 1: #If input is float
        element_to_count = float(element_to_count)
    print(f"Element {element_to_count} occured {my_list.count(element_to_count)} times in the list")
except ValueError as e:
    print(f"Invalid input: {e}")