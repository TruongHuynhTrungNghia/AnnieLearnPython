# BT4. Viết chương trình tính tổng, max, min một dãy có n số a0,a1,…, an-1
# a,n
# n=0 -> S(0)=0
# S(n)=a[n-1] + S(n-1)

a1 = [2, 3, 4]
a2 = [1, 2, 3, 4, 10, 20, 500]


def sum(a, n):
    # base case
    if n == 0:
        return 0
    # recursion case
    return a[n-1]+sum(a, n-1)
# findmax(a,n)
# n=1 -> max = a[0]
# n>1 if(a[n-1]> t=findmax(a,n-1)) -> a[n-1]  else


def findMax(a, n):
    if n == 1:
        return a[0]
    t = findMax(a, n=1)
    if a[n-1] > t:
        return a[n-1]
    else:
        return t


print(findMax(a2, len(a2)))
