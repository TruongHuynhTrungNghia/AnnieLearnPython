graph = {
    'A': {'B': 4, 'D': 6, 'G': 3},
    'B': {'C': 7, 'D': 5},
    'C': {'D': 1},
    'D': {'A': 1, 'E': 4, 'G': 1},
    'E': {'D': 2, 'F': 5},
    'F': {'G': 3},
    'G': {}
}


def DFS(grahp, u):
    visited = {}
    for k in grahp:
        visited[k] = 0
    stack = [u]
    visited[u] = 1
    while stack:
        u = stack.pop()
        for v in grahp[u]:
            if visited[v] == 0:
                visited[v] = 1
                stack.append(v)
    return visited


visited = DFS(graph, 'G')



def isConnected(visited):
    for k in visited:
        if visited[k] == 0:
            return False
    return True


def isGrahpConnected(grahp):
    for k in grahp:
        visited=DFS(grahp,k)
        if isConnected(visited)== False:
            return False
    return True

print(isConnected(visited))
print(isGrahpConnected(graph))