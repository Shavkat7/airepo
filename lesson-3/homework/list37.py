# Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.

# generate random list
my_list = [2, -3, 4, -15, 6, 6, -32, 432]

negative_sum = sum(x for x in my_list if x < 0)
print(f"Sum of negative numbers: {negative_sum}")
