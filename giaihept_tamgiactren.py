L=[
    [4,-3,1],
    [0,1,-3],
    [0,0,4]
]
b =[-4,-5,0]
n=len(b)
x=[0] * n 
for i in range(n-1,-1,-1):
    x[i] = b[i]
    for j in range(n-1,i,-1):
        x[i] -= L[i][j] * x[j]
    x[i] /= L[i][i]

print(x)
        