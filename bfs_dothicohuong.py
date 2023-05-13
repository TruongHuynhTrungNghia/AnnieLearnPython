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
    prev = {}
    dist = {}
    inf = 999999999
    for k in grahp:
        dist[k] = inf
        prev[k] = -1
    queue = [u]
    dist[u] = 0
    while queue:
        u = queue.pop(0)
        for v in grahp[u]:
            if dist[u] + grahp[u][v] < dist[v]:
                dist[v] = dist[u] + grahp[u][v]
                queue.append(v)
                prev[v] = u
    return prev, dist


prev, dist = DFS(graph, 'A')
print(prev)
print(dist)


def findPath(prev, dist, u, v):
    total = dist[v]
    print(v, end='')
    while v != u:
        t = prev[v]
        print('<-', t, end='')
        v = t
    print()
    return total


print(findPath(prev, dist, 'A', 'F'))
