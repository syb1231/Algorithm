from collections import deque
import sys
import copy
input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [-1,0,1,0]
ans = 1
def bfs(x,y,dir):
    global ans
    lotation = 0
    ndir = dir

    while(lotation < 4):
        ndir = (ndir + 3) % 4
        nx = x + dx[ndir]
        ny = y + dy[ndir]
        if(-1<nx<M and -1<ny<N and not info[ny][nx]):
            break
        lotation += 1
    if(lotation != 4):
        info[ny][nx] = 2 # 청소
        ans = ans + 1
        bfs(nx,ny,ndir)
    else:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if(-1<nx<M and -1<ny<N and info[ny][nx] != 1):
            bfs(nx,ny,dir)
    


N,M = map(int,input().split())
roy,rox,dir = map(int,input().split())
info = []
for i in range(N):
    info.append(list(map(int,input().split())))
info[roy][rox] = 2
bfs(rox,roy,dir)

print(ans)
