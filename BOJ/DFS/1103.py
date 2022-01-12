from collections import deque
import sys
sys.setrecursionlimit(250000)

def dfs(x,y):
    if(dp[y][x] != -1):
        return dp[y][x]

    dp[y][x] = 0

    d = int(info[y][x])
    dx = [-1*d,0,d,0]
    dy = [0,-1*d,0,d]
    maxDfs = [0,0,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(-1<nx<M and -1<ny<N and info[ny][nx] != 'H'):
            if(visted[ny][nx]):
                print(-1)
                exit()
            # if(dp[ny][nx] != -1):
            #     continue
            visted[ny][nx] = 1
            maxDfs[i] =  dfs(nx,ny)
            visted[ny][nx] = 0
    dp[y][x] = max(maxDfs) + 1
    return dp[y][x]
    

N,M = map(int, input().split())
info = [[0]*M for _ in range(N)]
dp= [[-1]*M for _ in range(N)]
visted = [[0]*M for _ in range(N)]

for i in range(N):
    tmp = str(sys.stdin.readline())
    for j in range(M):
        info[i][j]= tmp[j]

visted[0][0] = 1
print(dfs(0,0))
