num1 = int(input("Enter divident: "))
num2 = int(input("Enter divisor: "))

def check(func):
    try:
        print(func(num1, num2))
    except ZeroDivisionError:
        print("Denominator can't be zero")


@check                  # div = check(div)
def div(a, b):
   return a / b
