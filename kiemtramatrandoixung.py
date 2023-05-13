a =[
    [1,7,3],
    [7,4,5],
    [3,5,0]
]

b =[
    [1,2,3],
    [7,4,5],
    [3,5,0]
]

c =[
    [1,7,3],
    [7,4,5],
    [3,1,0]
]

def check(a):
    for i in range(len(a)):
        for j in range(i):
            if a[i][j] != a[j][i]:
                return False 
    return True 


print(check(a)) 
print(check(b)) 
print(check(c)) 