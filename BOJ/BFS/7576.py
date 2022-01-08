from collections import deque
import sys

dx = [-1,0,1,0]
dy = [0,-1,0,1]
dq = deque()

def yammyTomato():
    for y in range(N):
        for x in range(M):
            if(tomato[y][x] == 1 ):
                dq.append([x,y])

def zeroTomto():
    for y in range(N):
        for x in range(M):
            if(tomato[y][x] == 0 ):
                return 1
    return 0
                
def bfs():
    while(dq):
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx > -1 and nx < M and ny > -1 and ny < N and tomato[ny][nx] == 0):
                dq.append([nx,ny])
                tomato[ny][nx] = tomato[y][x] + 1
                
M,N = map(int, input().split())
tomato = []

for y in range(N):
    tomato.append(list(map(int,input().split())))

yammyTomato()
bfs()
if(zeroTomto()):
    print(-1)
    exit()
print(max(map(max, tomato)) -1)
