# Sum of Positive Numbers: Given a list of numbers, calculate the sum of all positive numbers.

# generate random list
my_list = [2, -3, 4, -15, 6, 6, -32, 432]

positive_sum = sum(x for x in my_list if x > 0)
print(f"Sum of positive numbers: {positive_sum}")
