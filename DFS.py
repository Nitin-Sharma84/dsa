graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

visited=set()
def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for n in graph[root]:
            dfs(visited,graph,n)


dfs(visited,graph,'A')
