# Filter Odd Numbers: Given a set of integers, create a new set that contains only the odd numbers.

my_set = {1, 2, 3, 4, 5, 6}
odd_set = set(filter(lambda x: x % 2 != 0, my_set))
print(odd_set)