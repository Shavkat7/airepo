# Filter Odd Numbers: Given a list of integers, create a new list that contains only the odd numbers.

# generate random list
my_list = [2, 3, 4, 15, 6, 6, 32, 432, 2, 4, 15]

odd_numbers = list(filter(lambda x: x % 2 != 0, my_list))
print(odd_numbers)
