L = [
    [2,0,0],
    [1,-3,0],
    [4,3,1]
]
b = [-4,-5,0]
n = len(b)
x=[0]*n 

for i in range(n):
    x[i]=b[i]
    for j in range(0,i):
        x[i]-=L[i][j]*x[j]
    x[i]/= L[i][i]
print(x)