graph = {
    'a':{'b':6,'c':8,'f':5},
    'b':{'a':6,'c':7,'e':3},
    'c':{'a':8,'b':7,'d':4},
    'd':{'c':4,'e':1,'f':1},
    'e':{'b':3,'d':1,'f':1},
    'f':{'a':5,'d':1,'e':1}
}
start = 'a'
end = 'd'
def DFS(start):
    stack = [start]
    visited = set()
    visited.add(start)
    prev = {}
    while len(stack)>0:
        node = stack.pop()
        for k in graph[node]:
            if k not in visited:
                stack.append(k)
                visited.add(k)
                prev[k] = node
    return prev

def findPath(prev,start,end):
    print(end, end = ' ')
    total = 0
    while end != start:
        t = prev[end]
        total += graph[end][t]
        print('<-',t,end = ' ')
        end = t 
    return total 

previous=DFS('a')
print(findPath(previous,'a','d'))