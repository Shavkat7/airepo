# Insert Element: Given a list and an element, insert the element at a specified index.

#generate any random list
my_list = [2, 3, 4, 15, "banana", 6, 6 ,32, "hello", 432, 2, 4, 15, "hello"]

element_to_insert = input("Enter an element to insert: ")


if element_to_insert.isdigit(): #If input is integer
        element_to_insert = int(element_to_insert)
elif element_to_insert.replace(".", "", 1).isdigit() and element_to_insert.count(".") == 1: #If input is float
    element_to_count = float(element_to_insert)

try:
    index_to_insert = int(input("Enter at which index you want to insert: "))
    my_list.insert(index_to_insert, element_to_insert)
    print(my_list)
except IndexError:
     print(f"Index is not corresponding with length of list {my_list}")
except ValueError:
     print("Index should be an integer")