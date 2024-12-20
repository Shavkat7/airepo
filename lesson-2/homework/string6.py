# Write a Python program to check if one string contains another.

str1 = input("Enter one string: ")
str2 = input("Ener another: ")
if str2.find(str1) != -1:
    print(True)
else:
    print(False)