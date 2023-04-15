def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return True
        return False


print(isPrime(3))
print(isPrime(5))
print(isPrime(10))
print(isPrime(7))
