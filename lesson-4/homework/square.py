
try:
    n = int(input("Enter a number: "))
    if n <= 0:
        print("Enter number more than 0")
    else:
        for i in range(1, n):
            print(i*i)
except ValueError:
    print("Enter only integer")
    