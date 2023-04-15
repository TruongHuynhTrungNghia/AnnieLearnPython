n = 3
label = [True]*n
a = [-1]*n
D = "abc"


def lietke(i):
    if i == n:
        for k in a:
            print(D[k],end="")
        print()
    else:
        for j in range(n):
            if label[j] == True:
                a[i] = j
                label[j] = False
                lietke(i+1)
                label[j] = True


lietke(0)
