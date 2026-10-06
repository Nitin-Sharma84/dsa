from collections import deque

start = "123456078"
goal = "123456780"

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def swap(state,zI,mI):
    state=list(state)#string immutable hai isliye list me conversion fir join krlenge
    state[zI],state[mI]=state[mI],state[zI]
    newState=''.join(state)
    return newState

    
def numBfs(start,goal,moves):
    q=deque()
    q.append(start)
    visited=set()
    visited.add(start)
    while q:
        currState=q.popleft()
        print(currState)
        if currState==goal:
            return 'Goal State found'
        
        zeroInd=currState.index('0')

        for move in moves[zeroInd]:
            newState=swap(currState,zeroInd,move)
            if newState not in visited:
                q.append(newState)
                visited.add(newState)
            
    return 'State not possible'
            

print(numBfs(start,goal,moves))











'''
def swap(state,zeroInd,moveInd):
    state=list(state)
    state[zeroInd],state[moveInd]=state[moveInd],state[zeroInd]
    return ''.join(state)

zeroInd=start.index('0')
print(zeroInd)

for i in moves[zeroInd]:
    newstate=swap(start,zeroInd, i)
    print(newstate)
    if newstate==goal:
        print("goal found")

'''
