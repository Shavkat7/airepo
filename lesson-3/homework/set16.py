# Filter Even Numbers: Given a set of integers, create a new set that contains only the even numbers.

my_set = {1, 2, 3, 4, 5, 6}
even_set = set(filter(lambda x: x % 2 == 0, my_set))
print(even_set)