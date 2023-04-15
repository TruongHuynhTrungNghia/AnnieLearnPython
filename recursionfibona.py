# BT2. Viết chương trình tình phần tử thứ n của dãy Fibonacci biết rằng phần tử thứ nhất bằng 0, phần tử thư 2 bằng 1, phân tử thứ n > 2 bằng tổng hai phần tử trước nó.
0, 1, 1, 2, 3, 5, 8


def fibo(n):
    # base case
    if n == 1:
        return 0
    if n == 2:
        return 1
    # Recursive case:
    return fibo(n-1)+fibo(n-2)


print(fibo(3))
print(fibo(5))
print(fibo(7))
