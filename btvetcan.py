S='MINHAA'
T='NAMNHI' 
def check(S,T): 
    arrS=list(S) + [0]
    n=len(S)
    labels=[0]*(n+1)
    for i in range(len(S)):
        arrS[n]=T[i]
        j=0 
        while arrS[j] != T[i] or labels[j]==1: #neu ky tu da duyet r thi di tim tiep ky tu tiep theo
            j += 1
        if j >=n:
            return False 
        else:
            labels[j]=1
    return True     

print(check(S,T))