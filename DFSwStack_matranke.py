#ma tran ke 
matrix=[
    [0,6,8,0,0,5],
    [6,0,7,0,3,0],
    [8,7,0,4,0,0],
    [0,0,4,0,1,1],
    [0,3,0,1,0,1],
    [5,0,0,1,1,0]
]
vertex = ['a','b','c','d','e','f'] 

def DFS(start):
    n = len(matrix)
    stack = [start]
    visited=[False]*n
    prev = [-1]*n 
    visited[start]=True
    while len(stack)>0:
        node=stack.pop()
        for i in range(n):
            if matrix[node][i] != 0 and visited[i]== False:
                stack.append(i)
                prev[i] = node 
                visited[i] = True
    return prev 

def findPath(prev,start,end):
    print(vertex[end],end=' ')
    total = 0
    while end != start:
        t=prev[end]
        print('->',vertex[t],end = ' ')
        total += matrix[end][t]
        end=t
    return total 

previous=DFS(0)
print(findPath(previous,0,3))