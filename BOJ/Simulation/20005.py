import sys 
from collections import deque
input=sys.stdin.readline
dirX = [-1,1,0,0]
dirY = [0,0,-1,1]

def bfs(palyer,info,n,m,p):
    toVisit = deque()
    visited = [[-1 for _ in range(n)] for _ in range(m)]
    for y in range(m):
        for x in range(n):
            if(info[y][x] == 'B'):
                toVisit.append([x,y])
                visited[y][x] = 0
                break
    
    while(toVisit):
        x,y = toVisit.popleft()
        if(info[y][x] != '.' and info[y][x] != 'X' and info[y][x] != 'B'):
            palyer[info[y][x]][1] = visited[y][x]


        for dirF in range(4):
            nx = x + dirX[dirF]
            ny = y + dirY[dirF]

            if(-1<nx<n and -1<ny<m and info[ny][nx] != 'X' and visited[ny][nx] == -1):
                visited[ny][nx] = visited[y][x] + 1
                toVisit.append([nx,ny])


m,n,p = map(int,input().split())
info = [list(input().strip()) for _ in range(m)]
palyer = {}

for i in range(p):
    tmp1, tmp2 = map(str,input().split())
    palyer[tmp1] = [int(tmp2),float('inf')]


bossHp = int(input())
bfs(palyer,info,n,m,p)
toCal = []
for p in palyer:
    toCal.append(palyer[p])

toCal.sort(key=lambda x:-x[1])

val = toCal.pop()
time = val[1]
hpBoom = val[0]
answer = 1
while(bossHp and toCal):
    val = toCal.pop()
    if(val[1] == float('inf')):
        break

    passedTime = val[1] - time
    bossHp -= passedTime*hpBoom

    if(bossHp>0):
        answer += 1
        time = val[1]
        hpBoom += val[0]
    else:
        break

print(answer)
