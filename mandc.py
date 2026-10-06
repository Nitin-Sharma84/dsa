# Missionaries and Cannibals using BFS (simple version)
# state = (m, c, b) : left bank pe m missionaries, c cannibals
# b = 1 matlab boat left pe, b = 0 matlab boat right pe

start = (3, 3, 1)
goal = (0, 0, 0)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

queue = [start]
parent = {start: None}      # visited bhi, path bhi

while queue:
    m, c, b = queue.pop(0)

    if (m, c, b) == goal:
        break

    for dm, dc in moves:
        if b == 1:                      # boat left pe, log right jaayenge
            nm, nc = m - dm, c - dc
        else:                           # boat right pe, log wapas aayenge
            nm, nc = m + dm, c + dc

        # safe check: range, left bank, right bank
        if 0 <= nm <= 3 and 0 <= nc <= 3:
            if (nm == 0 or nm >= nc) and (3 - nm == 0 or 3 - nm >= 3 - nc):
                new = (nm, nc, 1 - b)
                if new not in parent:
                    parent[new] = (m, c, b)
                    queue.append(new)

# goal se peeche chalke path nikalo
path = []
s = goal
while s is not None:
    path.append(s)
    s = parent[s]
path.reverse()

for s in path:
    print(s)
print("Total trips:", len(path) - 1)
