from collections import deque
from itertools import combinations
import sys
import copy
input = sys.stdin.readline
d = [[-1,0],[-1,-1],[-1,1],[0,1],[0,-1],[1,0],[1,-1],[1,1],[0,0]]
def bfs():
    toVisit = deque()
    visited = [[[0 for _ in range(8)] for _ in range(8)] for _ in range(16)]
    toVisit.append([0,7,0])
    while(toVisit):
        x,y,time = toVisit.popleft()
        if(x==7 and y==0):
            print(1)
            return
        if(y-time>-1 and wall[y-time][x]):
            continue
        for forward in d:
            nx = x + forward[0]
            ny = y + forward[1]
            if(-1<nx<8 and -1<ny<8 and not visited[time][ny][nx]):
                if(ny-time>-1 and wall[ny-time][nx]):
                    continue
                if(nx==7 and ny-time==0):
                    print(1)
                    return
                visited[time][ny][nx] = 1
                toVisit.append([nx,ny,time+1])
    print(0)


chess =[]
wall = [[0]*8 for _ in range(8)]
for i in range(8):
    chess.append(str(input()))
    for j in range(len(chess[i])):
        if(chess[i][j] == "#"):
            wall[i][j] = 1
bfs()
