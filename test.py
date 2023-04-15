n = 2
D = [0, 1]
S = [-1]*n
print(S)
e = []

# ham liet ke


def pagesNumbering(n):
    D = [0, 1]
    S = [-1]*n
    e = []

    def lietKe(i):
        if i == n:
            e.append(S)
        else:
            for j in D:
                S[i] = j
                lietKe(i+1)

        return len(e)

    print(lietKe(0))
