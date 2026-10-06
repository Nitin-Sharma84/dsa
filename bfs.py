from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


def bfs(start,path):
    q=deque()
    q.append(start)
    visited=set()
    visited.add(start)
    path.append(start)
    while q:
        cur=q.popleft()
        for i in graph[cur]:
            if i not in visited:
                visited.add(i)
                q.append(i)
                path.append(i)

    return path
path=[]
sol=bfs('A',path)

print(sol)
    
