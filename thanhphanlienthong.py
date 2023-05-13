grahp = {
    'A':['B','C'],
    'B':['A','C'],
    'C':['A','B','F'],
    'D':['G','H'],
    'F':['C'],
    'G':['D','H'],
    'H':['D','G']
}
def DFS(graph,visited,u,comp):
    stack=[u] 
    visited[u]=comp 
    while stack:
        u = stack.pop()
        for v in grahp[u]:
            if visited[v] ==0:
                visited[v]=comp
                stack.append(v)

visited = {}
for k in grahp:
    visited[k]=0
comp = 0    
for k in grahp: 
    if visited[k] == 0:
        comp +=1
        DFS(grahp,visited,k,comp)
print(visited)