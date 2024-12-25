# Repeat Elements: Given a list and a number, create a new list where each element is repeated that number of times.

# generate random list
my_list = [2, 3, 4, 15]

repeat_count = 3
repeated_list = [item for item in my_list for _ in range(repeat_count)]
print(repeated_list)
