# Check Palindrome: Given a list, check if the list is a palindrome (reads the same forwards and backwards).

# generate random list
my_list = [2, 3, 4, 3, 2]

is_palindrome = my_list == my_list[::-1]
print(f"Is the list a palindrome? {is_palindrome}")
