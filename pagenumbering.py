def pagesNumbering(n):
    D = [0, 1]
    S = [-1]*4
    count = []
    def listed(i):
        if i == n:
            count.append(S)
        else:
            for j in D:
                S[i] = j
                listed(i+1)      
    listed(0)
    return len(count)

pagesNumbering(1000)
