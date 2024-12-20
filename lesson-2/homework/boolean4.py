# Write a program that takes three numbers and checks if all of them are different.

num1 = int(input("number1: "))
num2 = int(input("number2: "))
num3 = int(input("number3: "))
print("are they all different?:", num1 != num2 and num1 != num3 and num2 != num3)