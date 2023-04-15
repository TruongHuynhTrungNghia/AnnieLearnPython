def digitsProduct(product):
    if product == 0:
        return 10
    s, p = 0, 1
    for v in range(9, 1, -1):
        while product % v == 0:
            s = v*p+s
            p *= 10
            product //= v
    if product != 1:
        return -1
    return s


print(digitsProduct(100))
print(digitsProduct(12))
print(digitsProduct(8))
