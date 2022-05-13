import sys 
from collections import deque
input=sys.stdin.readline
dirX = [-1,1,0,0,-1,-1,1,1,0]
dirY = [0,0,-1,1,-1,1,-1,1,0]

def bfs(n,m,info):
    startA = [-1,-1]
    startB = [-1,-1]
    for y in range(n):
        for x in range(m):
            if(info[y][x] == 'A'):
                startA = [x,y]
            elif(info[y][x] == 'B'):
                startB = [x,y]
    
    toVisit = deque()
    toVisit.append([startA[0],startA[1],startB[0],startB[1]])
    visted = [[[[ -1 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visted[startA[1]][startA[0]][startB[1]][startB[0]] = 0

    while(toVisit):
        ax,ay,bx,by = toVisit.popleft()
        if(ax == startB[0] and ay == startB[1] and bx == startA[0] and by == startA[1]):
            return visted[ay][ax][by][bx]

        for d1 in range(9):
            axn = ax + dirX[d1]
            ayn = ay + dirY[d1]

            if(axn<0 or axn>m-1 or ayn<0 or ayn>n-1 or info[ayn][axn] == 'X'):
                continue

            for d2 in range(9):
                bxn = bx + dirX[d2]
                byn = by + dirY[d2]

                if(d1 == 8 and d2 == 8):
                    continue
                if(bxn<0 or bxn>m-1 or byn<0 or byn>n-1 or info[byn][bxn] == 'X'):
                    continue
                if(axn == bx and ayn == by and bxn == ax and byn == ay):
                    continue
                if(axn == bxn and ayn == byn):
                    continue


                if(visted[ayn][axn][byn][bxn] == -1):
                    toVisit.append([axn,ayn,bxn,byn])
                    visted[ayn][axn][byn][bxn] = visted[ay][ax][by][bx] + 1
        
        for d1 in range(8):
            axn = ax + dirX[d1]
            ayn = ay + dirY[d1]        

    return -1
            

            



        

n,m = map(int,input().split())
info = [list(input().strip()) for _ in range(n)]
print(bfs(n,m,info))
