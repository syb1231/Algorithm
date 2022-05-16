import sys
from collections import deque
input = sys.stdin.readline
dirF = [[-1,0],[1,0],[0,1],[0,-1]]
def bfs(x,y,info,visited):
    
    toVisit2 = deque()
    toVisit2.append([x,y])
    visited[y][x] = 1
    cnt = 1
    while(toVisit2):
        x,y = toVisit2.popleft()
        for i in range(4):
            nx = x + dirF[i][0]
            ny = y + dirF[i][1]

            if(nx<0 or nx>m-1 or ny<0 or ny>n-1):
                continue

            if(not visited[ny][nx]):
                cnt += 1
                toVisit2.append([nx,ny])
                visited[ny][nx] = 1

    return cnt




n,m = map(int,input().split())
info = []
for i in range(n):
    info.append(list(map(int,input().split())))

toVisit = deque()
for y in range(n):
    for x in range(m):
        if(info[y][x]):
            toVisit.append([x,y,info[y][x]])

ans = 1
visited = [[1 for _ in range(m)] for _ in range(n)]
while(toVisit):
    size = len(toVisit)
    
    for i in range(size):
        x,y,val = toVisit.popleft()
        cnt = 0
        for d in range(4):
            nx = x + dirF[d][0]
            ny = y + dirF[d][1]

            if(nx<0 or nx>m-1 or ny<0 or ny>n-1):
                continue
            if(not info[ny][nx]):
                cnt += 1
        
        if(val-cnt<0):
            val = 0
        else:
            val -= cnt
        toVisit.append([x,y,val])
    
    cnt = 0
    for i in range(size):
        x,y,val = toVisit.popleft()
        info[y][x] = val
        if(val):
            visited[y][x] = 0
            cnt += 1
            toVisit.append([x,y,val])
    ck = False
    for y in range(n):
        if(ck):
            break
        for x in range(m):
            if(info[y][x]):
                if(cnt != bfs(x,y,info,visited)):
                    print(ans)
                    exit()
                ck = True
                break
    ans += 1
    
print(0)
            


