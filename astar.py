graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 6)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

h = {
    'A': 7, 'B': 6, 'C': 4, 'D': 3, 'E': 2, 'F': 1, 'G': 0
}

def astar(start, goal, graph, h):
    open_list = [(h[start], 0, start, [start])]  # (f, g, node, path)
    visited = set()

    while open_list:
        # manually find node with smallest f
        best = open_list[0]
        for item in open_list:
            if item[0] < best[0]:
                best = item

        open_list.remove(best)

        f, g, current, path = best
        
        if current == goal:
            return path, g

        if current in visited:
            continue
        
        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor in visited:
                continue
            new_g = g + cost
            new_f = new_g + h[neighbor]
            open_list.append((new_f, new_g, neighbor, path + [neighbor]))

    return "Path not found!", None

path, cost = astar('A', 'G', graph, h)
print("Path:", path)
print("Cost:", cost)
