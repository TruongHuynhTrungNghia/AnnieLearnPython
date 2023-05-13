L=[
    [2,0,0],
    [1,-3,0],
    [3,4,1]
]

U=[
    [4,-3,1],
    [0,1,-1],
    [0,0,4]
] 

b = [-4,5,0]

def lower(L,b):
    n = len(b)
    x=[0]*n 

    for i in range(n):
        x[i]=b[i]
        for j in range(0,i):
            x[i]-=L[i][j]*x[j]
        x[i]/= L[i][i]
    return x

def upper(U,b):
    n=len(b)
    x=[0] * n 
    for i in range(n-1,-1,-1):
        x[i] = b[i]
        for j in range(n-1,i,-1):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]    
    return x 

#LUX=b
#L(UX)=b
#UY=b=>Y
#LY=b
def solve(L,U,b):
    y = lower(L,b)
    x = upper(U,y)
    return x    

print(solve(L,U,b))