graph = {
    'a': {'b': 6, 'c': 8, 'f': 5},
    'b': {'a': 6, 'c': 7, 'e': 3},
    'c': {'a': 8, 'b': 7, 'd': 4},
    'd': {'c': 4, 'e': 1, 'f': 1},
    'e': {'b': 3, 'd': 1, 'f': 1},
    'f': {'a': 5, 'd': 1, 'e': 1}
}


def DFS(grahp, u):
    prev = {}
    dist = {}
    inf = 999999999
    for k in grahp:
        dist[k] = inf
        prev[k] = -1
    stack = [u]
    dist[u] = 0
    while stack:
        u=stack.pop()
        for v in grahp[u]:
            if dist[u] + grahp[u][v] < dist[v]:
                dist[v] = dist[u] + grahp[u][v]
                stack.append(v)
                prev[v] = u
    return prev, dist


prev, dist = DFS(graph, 'a')
print(prev)
print(dist)

def findPath(prev,dist,u,v):
    total = dist[v]
    print(v,end='')
    while v != u:
        t = prev[v]
        print('<-',t,end='')
        v = t 
    print()
    return total 
print(findPath(prev,dist,'a','e'))