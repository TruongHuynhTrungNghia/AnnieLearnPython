D=['tao','le','xoai']
n = len(D)
k = 2
a = [-1]*(k+1)

def lietke(i):
    if i > k:
        #print(a[1:])
        print([D[k] for k in a[1:]])
    else:
        for j in range(a[i-1]+1, n-k+i):
            a[i] = j
            lietke(i+1)


lietke(1)
