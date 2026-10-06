from collections import deque

A = 4
B = 3
goal = 2

queue = deque()
queue.append((0, 0))

visited = set()
visited.add((0, 0))

parent = {}

while queue:

    a, b = queue.popleft()

    if a == goal:
        break

    states = [
        (A, b),                     
        (a, B),                     
        (0, b),                     
        (a, 0),                     
        (a - min(a, B-b), b + min(a, B-b)),  
        (a + min(b, A-a), b - min(b, A-a))   
    ]

    for state in states:

        if state not in visited:
            visited.add(state)
            queue.append(state)
            parent[state] = (a, b)


# Print path
path = []
state = (a, b)

while state != (0, 0):
    path.append(state)
    state = parent[state]

path.append((0, 0))

path.reverse()

for state in path:
    print(state)
