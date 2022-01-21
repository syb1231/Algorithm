from collections import deque
import sys
import copy
input = sys.stdin.readline
forwardDir = [[0,-1],[1,0],[0,1],[-1,0]]
def forwarding(dir,x,y,anotherx,anothery):
    nx = x + forwardDir[dir][0]
    ny = y + forwardDir[dir][1]
    while(-1<nx<M and -1<ny<N):
        if(info[ny][nx] == 'O'):
            return -1,-1
        if(info[ny][nx] == '.' and not (nx == anotherx and ny == anothery)):
            nx = nx + forwardDir[dir][0]
            ny = ny + forwardDir[dir][1]
        else:
            break
    return nx-forwardDir[dir][0],ny-forwardDir[dir][1]     


def bfs():
    tovisit = deque()
    tovisit.append([red[0],red[1],blue[0],blue[1],0,0])
    tovisit.append([red[0],red[1],blue[0],blue[1],1,0])
    tovisit.append([red[0],red[1],blue[0],blue[1],2,0])
    tovisit.append([red[0],red[1],blue[0],blue[1],3,0])

    while(tovisit):
        redx,redy,bluex,bluey,dir1,count = tovisit.popleft()
        visited[dir1][redx*nmMax + redy][bluex*nmMax + bluey] = 1
        # if(count == 10):
        #     continue
        whoFirst = 0
        if(dir1==0 and redy < bluey):
            whoFirst = 1
        elif(dir1==1 and redx > bluex):
            whoFirst = 2    
        elif(dir1==2 and redy > bluey):
            whoFirst = 3    
        elif(dir1==3 and redx < bluex):
            whoFirst = 4    
        if(not whoFirst):
            nbluex,nbluey = forwarding(dir1,bluex,bluey,-1,-1)
            if(nbluex == -1):
                continue
            nredx,nredy = forwarding(dir1,redx,redy,nbluex,nbluey)
            if(nredx == -1):
                return count+1
        else:
            nredx,nredy = forwarding(dir1,redx,redy,-1,-1)
            nbluex,nbluey = forwarding(dir1,bluex,bluey,nredx,nredy)
            if(nbluex == -1):
                continue
            if(nredx == -1):
                return count+1
        for ndir in range(4):
            if(not visited[ndir][nredx*nmMax + nredy][nbluex*nmMax + nbluey]):
                tovisit.append([nredx,nredy,nbluex,nbluey,ndir,count+1])
    return -1

N,M = map(int,input().split())
red = [0,0]
blue = [0,0]
nmMax = max(N,M)
visited = [[[0 for _ in range(nmMax**2)] for _ in range(nmMax**2)] for _ in range(4)]
info = []
for y in range(N):
    info.append(list(input()))
    for x in range(M):
        if(info[y][x]=="R"):
            info[y][x] = '.'
            red = [x,y]
        elif(info[y][x]=="B"):
            info[y][x] = '.'
            blue = [x,y]
print(bfs())
