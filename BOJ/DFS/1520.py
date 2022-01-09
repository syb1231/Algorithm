from collections import deque
import sys
sys.setrecursionlimit(100000)
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def dfs(x,y):
    if(dp[y][x]!=-1):
        return dp[y][x]
    dp[y][x]=0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(-1<nx<M and -1<ny<N and info[y][x] < info[ny][nx]):
            dp[y][x] = dp[y][x] + dfs(nx,ny)
    return dp[y][x]

N,M = map(int,input().split())
info = []
for i in range(N):
    info.append(list(map(int,input().split())))
dp = [[-1]*M for _ in range(N)]
dp[0][0] =1
#print(dfs(1,0))
print(dfs(M-1,N-1))
