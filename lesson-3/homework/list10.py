# Sort List: Create a new list that contains the elements of the original list in sorted order.

#generate any random list
my_list = [85, 76, 9.89, 56, 23, 45, 56, -45]

try:
    print(sorted(my_list))
except TypeError:
    print(f"The list {my_list} contains some non-numerical values")