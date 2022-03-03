from collections import deque
from itertools import combinations
import sys
import copy
import heapq
import math
input = sys.stdin.readline
ndir = [[0]*4 for i in range(5)]
ndir[1] = [2,1,0,3]
ndir[2] = [0,3,2,1]
ndir[3] = [3,2,1,0]
ndir[4] = [1,0,3,2]

dirForward = [[-1,0],[0,-1],[1,0],[0,1]]
def cal(dirN,x,y):
    global info
    global infoForAns
    global visited
    infoForAns[y][x] = 1
    visited[y][x][dirN] = 1
    nextDir = dirN
    if(info[y][x]):
        nextDir = ndir[info[y][x]][dirN]
    nx = x + dirForward[nextDir][0]
    ny = y + dirForward[nextDir][1]
    if(-1<nx<m and -1<ny<n and not visited[ny][nx][nextDir]):
        return 1,nextDir,nx,ny
    return 0,nextDir,nx,ny


n,m = map(int,input().split())
info = []
aircon = []
infoForAns = [[0]*m for _ in range(n)]

for i in range(n):
    info.append(list(map(int,input().split())))

for y in range(n):
    for x in range(m):
        if(info[y][x] == 9):
            aircon.append([x,y])
            info[y][x] = 0

visited =[[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]
for a in aircon:
    keepGo,nextDir,nx,ny = cal(0,a[0],a[1])
    while(keepGo):
        keepGo,nextDir,nx,ny = cal(nextDir,nx,ny)

    keepGo,nextDir,nx,ny = cal(1,a[0],a[1])
    while(keepGo):
        keepGo,nextDir,nx,ny = cal(nextDir,nx,ny)

    keepGo,nextDir,nx,ny = cal(2,a[0],a[1])
    while(keepGo):
        keepGo,nextDir,nx,ny = cal(nextDir,nx,ny)

    keepGo,nextDir,nx,ny = cal(3,a[0],a[1])
    while(keepGo):
        keepGo,nextDir,nx,ny = cal(nextDir,nx,ny)

ans = 0

for y in range(n):
    for x in range(m):
        ans += infoForAns[y][x]
print(ans)


        
# 오래만에 해서 그런가 감이 안 잡혔어서 시간을 너무 많이 잡아 먹었음, 매일 매일 문제 풀자
