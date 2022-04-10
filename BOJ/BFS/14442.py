import sys
import math
from collections import deque
#sys.setrecursionlimit(100000)
input = sys.stdin.readline
dirForward = [[0,1],[0,-1],[-1,0],[1,0]]
def bfs(info,k,n,m):
    visited = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    toVistit = deque()
    toVistit.append([0,0,k])
    visited[0][0][k] = 1
    while(toVistit):
        x,y,left = toVistit.popleft()
        if(x == m-1 and y == n-1):
            return visited[y][x][left]
        for dir1 in dirForward:
            nx = x + dir1[0]
            ny = y + dir1[1]
            if(-1<nx<m and -1<ny<n):
                if(info[ny][nx]):
                    if(left and not visited[ny][nx][left-1]):
                        visited[ny][nx][left-1] = visited[y][x][left] + 1
                        toVistit.append([nx,ny,left-1])
                else:
                    if(not visited[ny][nx][left]):
                        visited[ny][nx][left] = visited[y][x][left] + 1
                        toVistit.append([nx,ny,left])
    return -1

                        


n,m,k = map(int,input().split())

tmp = []
info = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    tmp.append(str(input()))

for y in range(n):
    for x in range(m):
        info[y][x] = int(tmp[y][x])

print(bfs(info,k,n,m))
