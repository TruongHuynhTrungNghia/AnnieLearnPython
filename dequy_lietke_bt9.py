# BT9. Viết chương trình liệt kê các chuỗi nhị phân n bit.
n = 4
D = [0, 1]
S = [-1]*4
print(S)

# ham liet ke


def lietKe(i):
    if i == n:
        print(S)
    else:
        for j in D:
            S[i] = j
            lietKe(i+1)


lietKe(0)
