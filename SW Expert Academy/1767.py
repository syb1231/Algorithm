import copy
forwardDir = [[-1,0],[0,-1],[1,0],[0,1]]
def forwarding(x,y,dir1):
    while(-1<x<n and -1<y<n):
        visited[y][x] = 1
        x = x + forwardDir[dir1][0]
        y = y + forwardDir[dir1][1]


# def getCost(x,y):
#     tmp = [[x,0],[y,1],[n-x-1,2],[n-y-1,3]]
#     tmp.sort(key=lambda x:x[0])
#     for i in tmp:
#         if(forwardingCheck(x,y,i[1])):
#             return i[0]
#     return 0

def forwardingCheck(index):
    for dir1 in range(4):
        nx,ny = core[index]
        while(True):
            nx = nx + forwardDir[dir1][0]
            ny = ny + forwardDir[dir1][1]
            if(-1<nx<n and -1<ny<n):
                if(info[ny][nx]):
                    break
            else:
                possibleDir[index][dir1] = 1
                break


def forwarding(startx,starty,dire):
    nx = startx
    ny = starty
    counting = 0
    while(True):
        nx = nx + forwardDir[dire][0]
        ny = ny + forwardDir[dire][1]
        if(-1<nx<n and -1<ny<n):
            if(visited[ny][nx]):
                return 0,nx,ny,counting
            visited[ny][nx] = 1
            counting += 1
        else:
            return 1,nx,ny,counting

def backForwrding(startx,starty,endx,endy,dire):
    nx = startx
    ny = starty
    while(True):
        nx = nx - forwardDir[dire][0]
        ny = ny - forwardDir[dire][1]
        if(nx == endx and ny == endy):
            return 
        else:
            visited[ny][nx] = 0

def dfs(index,coreCount,countSum,):
    global ansTmp 
    if(index == len(core)):
        if(ansTmp[0] < coreCount):
            ansTmp[0] = coreCount
            ansTmp[1] = countSum
        elif(ansTmp[0] == coreCount and ansTmp[1] > countSum):
            ansTmp[1] = countSum
        return
    if(coreCount + (len(core) - index) < ansTmp[0]):
        return
    for dir1 in range(4):
        if(possibleDir[index][dir1]):
            result = forwarding(core[index][0],core[index][1],dir1)
            #print(core[index][0],core[index][1],dir1,result)
            if(result[0]):
                dfs(index+1,coreCount+1,countSum+result[3])
            backForwrding(result[1],result[2],core[index][0],core[index][1],dir1)
    dfs(index+1,coreCount,countSum)
    


t = int(input())
ans = []

for testCase in range(t):
    n = int(input())
    info = []
    visited = [[0]*n for _ in range(n)]
    core = []
    ansTmp = [0,0]
    for i in range(n):
        info.append(list(map(int,input().split())))
    
    for y in range(n):
        for x in range(n):
            if(info[y][x] == 1):
                visited[y][x] = 1
                if(x==0 or x== n-1 or y==0 or y==n-1):
                    continue
                core.append([x,y])
    possibleDir = [[0]*4 for _ in range(len(core))]
    for i in range(len(core)):
        forwardingCheck(i)
    dfs(0,0,0)
    ans.append(ansTmp[1])

for testCase in range(t):
    print('#',end="")
    print(testCase+1,end=" ")
    print(ans[testCase])
