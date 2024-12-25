# Remove Element by Index: Given a list and an index, remove the element at that index if it exists.

# generate random list
my_list = [2, 3, 4, 15, "banana", 6, 6, 32, "hello", 432, 2, 4, 15]

try:
    index_to_remove = int(input("Enter the index to remove: "))
    my_list.pop(index_to_remove)
    print(my_list)
except IndexError:
    print(f"Index out of range. List length is {len(my_list)}")
except ValueError:
    print("Please enter a valid integer index.")
