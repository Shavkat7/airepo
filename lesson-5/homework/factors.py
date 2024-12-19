number1 = int(input("Enter a positive integer:"))
def factorize(number):
    if number <= 0:
        print("It is not positive!")
        return
    if type(number) != int:
        print("It is not an integer!")
        return
    for i in range(1, int(number/2+1)):
        if number % i == 0:
            print(f"{i} is a factor of {number}")
            
factorize(number1)