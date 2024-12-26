def isPrime(n: int):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

try:
    limit = int(input("Enter upper boundary of prime numbers list: "))
    if limit < 0: raise ValueError
    for i in range(2, limit):
        if isPrime(i):
            print(i)
except ValueError:
    print("Enter a POSITIVE INTEGER")