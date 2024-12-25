# Count Odd Numbers: Given a list of integers, count how many of them are odd.

#generate any random list
my_list = [2, 3, 4, 15, 6, 6 ,32, 432, 2, 4, 15, -10]

odd_values_number = len(list(filter(lambda x: x % 2 != 0, my_list)))
print(odd_values_number)