# Replace Element: Given a list, replace the first occurrence of a specified element with another element.

#generate random list
my_list = [2, 3, 4, 15, "banana", 6, 6 ,32, "hello", 432, 2, 4, 15, "hello"]

try:
    old_element = input("Enter element to be replaced: ")
    new_element = input("Enter element to insert: ")

    if old_element.isdigit(): #If input is integer
        old_element = int(old_element)
    elif old_element.replace(".", "", 1).isdigit() and old_element.count(".") == 1: #If input is float
        element_to_count = float(old_element)

    index_to_insert = my_list.index(old_element)
    my_list.remove(old_element)
    my_list.insert(index_to_insert, new_element)
    print(my_list)
except IndexError:
    print("Incorrect index")
except ValueError:
    print("Incorrect value")