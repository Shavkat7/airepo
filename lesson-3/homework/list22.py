# Filter Even Numbers: Given a list of integers, create a new list that contains only the even numbers.

# generate random list
my_list = [2, 3, 4, 15, 6, 6, 32, 432, 2, 4, 15]

even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
print(even_numbers)
