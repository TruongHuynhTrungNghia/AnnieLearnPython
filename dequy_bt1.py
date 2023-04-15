def C(k, n):
    if k == 0 or k == n:
        return 1
    return C(k, n-1) + C(k-1, n-1)


print(C(2, 4))
print(C(2, 5))
