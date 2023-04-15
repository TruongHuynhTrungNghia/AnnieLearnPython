# BT5. Một dãy được gọi là có thứ tự tăng (giảm) nếu ai > ai+1 (hay <). Viết chương trình kiểm tra dãy a0,…, an-1 có phải dãy tăng.
# isGreater(n,a)
# a[n-1] lớn hơn a[n-2]
# n==1 --> true
# n>1, if isGreater(a[n-1],a(n-1)) == true
a2 = [1, 2, 3,11,4, 10, 20, 500]


def isGreater(a, n):
    if n == 1:
        return True
    if a[n-1] < a[n-2]:
        return False
    return isGreater(a, n-1)


print(isGreater(a2, len(a2)))
