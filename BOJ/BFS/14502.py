from collections import deque
from itertools import combinations
import sys
import copy
dx = [-1,0,1,0]
dy = [0,-1,0,1]

potenwall = deque()     
initVirus = deque()
def bfs(newWall):
    dq = copy.deepcopy(initVirus)
    tmpInfo = copy.deepcopy(info) 
    tmpInfo[newWall[0][1]][newWall[0][0]] = 1
    tmpInfo[newWall[1][1]][newWall[1][0]] = 1
    tmpInfo[newWall[2][1]][newWall[2][0]] = 1

    while(dq):
        x,y = dq.popleft()    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if( -1<nx<M and -1<ny<N and tmpInfo[ny][nx] == 0):
                dq.append([nx,ny])
                tmpInfo[ny][nx] = 2
    return checkAns(tmpInfo)

def checkAns(tmpInfo):
    cnt = 0
    for y in range(N):
        for x in range(M):
            if(tmpInfo[y][x] == 0):
                cnt = cnt +1
    return cnt

def potentialWall():
    for y in range(N):
        for x in range(M):
            if (info[y][x] == 0):
                potenwall.append([x,y])
            if(info[y][x] == 2):
                initVirus.append([x,y])
ans = -1
N,M = map(int, input().split())
info = []
for y in range(N):
    info.append(list(map(int,input().split())))

potentialWall()
combination = list(combinations(potenwall, 3))

for i in combination:
    zeroCount = bfs(i)
    if(ans < zeroCount):
        ans = zeroCount

print(ans)
