a = [
    [1,2,3],
    [2,1,1],
    [1,1,1]
    
]
b = [
    [0,1,1],
    [1,1,1],
    [1,2,1]
] 

def summatrix(a,b):
#    sumab= [[0]*len(a[0])]*len(a)  
    sumab = []  
    for i in range(len(a)):
        sumab.append([0]*len(a[i]))
    for i in range(len(a)):
        for j in range(len(a[i])):
            sumab[i][j]=a[i][j]+b[i][j]
    return sumab 

print(summatrix(a,b))

sumab1 = [[0]*3]*2
print(sumab1)
sumab1[0][0]=4
print(sumab1)
