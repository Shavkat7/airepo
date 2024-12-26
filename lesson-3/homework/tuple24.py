# Check Palindrome: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).

# Generate a random tuple
my_tuple = (1, 5, 7, 5, 1)

is_palindrome = my_tuple == my_tuple[::-1]
print(is_palindrome)