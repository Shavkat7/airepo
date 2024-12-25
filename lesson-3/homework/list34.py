# Rotate List: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).

# generate random list
my_list = [2, 3, 4, 15, 6, 6, 32]

n = 2  # number of positions to rotate
rotated_list = my_list[-n:] + my_list[:-n]
print(rotated_list)
