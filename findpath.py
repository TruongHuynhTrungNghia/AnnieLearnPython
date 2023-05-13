def findPath(prev,dist,u,v):
    total = dist[v]
    print(v,end='')
    while v != u:
        t = prev[v]
        print('<-',t,end='')
        v = t 
    return total 
print(findPath(prev,dist,'a','e'))