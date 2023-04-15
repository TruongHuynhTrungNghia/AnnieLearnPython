def greatestCommonPrimeDivisor(a, b):
    def prime_factor(n):
        pfactor = []
        for i in range(2, int(n**0.5)+1):
            while n % i == 0:
                pfactor.append(i)
                n = n/i
        if n > 1:
            pfactor.append(int(n))
        else:
            return pfactor
        return pfactor
    gCPD = set(prime_factor(a)) & set(prime_factor(b))
    if gCPD:
        return max(gCPD)
    else:
        return -1


print(greatestCommonPrimeDivisor(12, 18))
