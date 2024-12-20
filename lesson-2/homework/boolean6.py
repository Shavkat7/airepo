# Create a program that accepts a number and checks if it’s divisible by both 3 and 5.

num1 = int(input("enter a number: "))
print("Is it divisible by both 3 and 5?:", num1 % 3 == 0 and num1 % 5 ==0)