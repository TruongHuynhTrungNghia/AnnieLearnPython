# BT6. Viết chương trình kiểm cho biết vị tri của một giá trị x trong danh sách a0, a1,…, an-1 (kết quả = -1 nếu x không có trong danh sách).
# isFind(x,a,n)
# n==0 --> -1
# if n=>0, a[n-1]==x return n-1
# else isFind(x,a,n-1)
a2 = [1, 2, 3, 11, 4, 10, 20, 500]
x1 = 10
x2 = 12


def isFind(x, a, n):
    if n == 0:
        return -1
    if a[n-1] == x:
        return n-1
    return isFind(x, a, n-1)


print(isFind(x2, a2, len(a2)))
