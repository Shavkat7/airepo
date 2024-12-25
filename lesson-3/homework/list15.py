# Count Even Numbers: Given a list of integers, count how many of them are even.

#generate any random list
my_list = [2, 3, 4, 15, 6, 6 ,32, 432, 2, 4, 15, -10]

even_values_number = len(list(filter(lambda x: x % 2 == 0, my_list)))
print(even_values_number)