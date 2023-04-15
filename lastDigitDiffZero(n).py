def lastDigitDiffZero(n):
    N = 1
    for i in range(1, n+1, 1):
        N = N * i
    # while N % 10 == 0:
        # N = N // 10
    for i in range(len(str(N))-1, -1, -1):
        j = str(N)[i]
        if j != "0":
            return int(j)


print(lastDigitDiffZero(10))
