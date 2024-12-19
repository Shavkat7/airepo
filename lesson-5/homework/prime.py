def is_prime(n):
    if n <= 0:
        return "It is not positive"
    if type(n) != int:
        return "It is not integer"
    if n == 1:
        return "1 is not prime nor not-prime"
    for i in range(2, int(n/2+1)):
        if n % i == 0:
            return False
    return True

print(is_prime(10))