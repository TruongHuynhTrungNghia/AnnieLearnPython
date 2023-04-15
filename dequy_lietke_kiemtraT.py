a = [2, 3, 4, 5, 7]
T = 7
n = len(a)
S = [-1]*n
print(S)
D = [0, 1]


def Tong(a, b):
    s = 0
    for i in range(n):
        s = s+(a[i]*b[i])
    return s


def lietke(i):
    if i == n:
        if Tong(a, S) == T:
            for k in range(n):
                if S[k] == 1:
                    print(a[k],end=" ")
            print()        
    else:
        for j in D:
            S[i] = j
            lietke(i+1)


lietke(0)
