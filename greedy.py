# Greedy-Best-First-Search(start, goal):

# 1. Put start node into OPEN list.
# 2. Set CLOSED list = empty.

# 3. While OPEN is not empty:
#       a. Select the node n from OPEN
#          having the smallest h(n).

#       b. If n is the goal:
#              return the solution/path.

#       c. Remove n from OPEN.
#       d. Add n to CLOSED.

#       e. Generate all successors of n.
#       f. For each successor:
#              If it is not in OPEN or CLOSED:
#                  calculate h(successor)
#                  add it to OPEN.

# 4. If OPEN becomes empty:
#       return failure.

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Heuristic values
h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

def greedy(s,g,graph,h):
    path=[]
    current=s
    open_list=deque()
    open_list.append(current)
    while open_list:
        for node in open_list:
            if h[node]< h[current]:
                current=node
                
        path.append(current)
        if current==g:
            return path

        open_list.remove(current)
        for node in graph[current]:
            open_list.append(node)

    return "Path not found!"

path=greedy('A','G',graph,h)

print(path)
