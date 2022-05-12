import sys
from collections import deque
from itertools import combinations
def bfs(info,n,m):
    toVisit = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if(info[y][x] == 'W'):
                toVisit.append([x,y])
                visited[y][x] = 1
    
    while(toVisit):
        x,y = toVisit.popleft()
        for i in range(4):
            nx = x + dirFoward[i][0]
            ny = y + dirFoward[i][1]

            if(info[ny][nx] == '#'):
                continue

            while(info[ny][nx] == "+"):
                nx = nx + dirFoward[i][0]
                ny = ny + dirFoward[i][1]
            if(info[ny][nx] == "#"):
                    nx = nx - dirFoward[i][0]
                    ny = ny - dirFoward[i][1]

            if(not visited[ny][nx]):
                toVisit.append([nx,ny])
                visited[ny][nx] = 1               

    for y in range(n):
        for x in range(m):
            if(info[y][x] == "." and not visited[y][x]):
                print('P',end="")
            else:
                print(info[y][x],end="")
        print("")


    

input = sys.stdin.readline
dirFoward = [[-1,0],[1,0],[0,-1],[0,1]]
n,m =map(int,input().split())
info = [list(input().strip()) for _ in range(n)]
bfs(info,n,m)
