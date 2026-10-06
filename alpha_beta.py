tree={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[4,1],
    'E':[9,7],
    'F':[3,8],
    'G':[1,2]
    }

def alpha_beta(node,depth,alpha,beta,player):
    if depth==0:
        if node in tree:
            return tree[node][0]
        else:
            return node

    if player:
        value=float('-inf')
        for child in tree[node]:
            value=max(value,alpha_beta(child,depth-1,alpha,beta,False))
            alpha=max(alpha,value)
            if alpha>=beta:
                print(f"Pruning at {node}")
                return value
        return value

    else:
        value=float('inf')
        for child in tree[node]:
            value=min(value,alpha_beta(child,depth-1,alpha,beta,True))
            beta=min(beta,value)
            if alpha>=beta:
                print(f"Pruning at {node}")
                return value
        return value
    
val=alpha_beta('A',3,float('-inf'),float('inf'),True)
print(val)
