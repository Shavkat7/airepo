# Create a program to ask name and year of birth from user and tell them their age.

from datetime import datetime

name = input("Enter your name: ")
year = int(input("Year you are born in: "))
print(f"{name}, you are {datetime.now().year - year} years old!")