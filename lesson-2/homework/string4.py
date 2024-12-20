# Write a Python program to check if a given string is palindrome or not.

# What is a Palindrome String? 
# A string is called a palindrome if the reverse of the string is the same as the original one. 
# Example: “madam”, “racecar”, “12321”.

inp = input("enter a word: ")

if inp[::] == inp[::-1]:
    print(f"{inp} is a palindrome")
else:
    print(f"{inp} is not a palindrome")