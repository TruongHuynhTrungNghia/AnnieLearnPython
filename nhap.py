n = 4
D = [0, 1]
S = [-1]*n


def lietke(i):
    if n == i:
        print(S)
    else:
        for j in D:
            S[i] = j
            lietke(i+1)
