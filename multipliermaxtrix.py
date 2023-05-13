a = [
    [1,2],
    [2,1],
    [1,1]
]
b = [
    [0,1,1],
    [1,1,2],
] 

def multiplyMatrix(a,b):
    c=[]
    for i in range(len(a)):
        c.append([0]*len(b[0]))
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b[0])):
                c[i][k] += a[i][j] * b[j][k]
    return c            
print(multiplyMatrix(a,b))