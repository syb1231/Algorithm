import sys
from collections import deque
import heapq
input = sys.stdin.readline
dirForward = [[] for _ in range(8)]
dirForward[0] = [[-1,0],[-1,-1],[-1,-1]]
dirForward[1] = [[-1,0],[-1,1],[-1,1]]
dirForward[2] = [[1,0],[1,1],[1,1]]
dirForward[3] = [[1,0],[1,-1],[1,-1]]
dirForward[4] = [[0,-1],[-1,-1],[-1,-1]]
dirForward[5] = [[0,-1],[1,-1],[1,-1]]
dirForward[6] = [[0,1],[-1,1],[-1,1]]
dirForward[7] = [[0,1],[1,1],[1,1]]


def bfs(shang,king):
    visited = [[-1]*10 for _ in range(9)]
    toVisit = deque()
    visited[shang[1]][shang[0]] = 0
    toVisit.append([shang[0],shang[1]])
    while(toVisit):
        x,y = toVisit.popleft()

        if( x== king[0] and y == king[1]):
            print(visited[y][x])
            exit()

        for dir1 in range(8):
            nx = x + dirForward[dir1][0][0]
            ny = y + dirForward[dir1][0][1]
            if(-1<nx<10 and -1<ny<9 and not(nx == king[0] and ny ==king[1])):
                nx = nx + dirForward[dir1][1][0]
                ny = ny + dirForward[dir1][1][1]
                if(-1<nx<10 and -1<ny<9 and not(nx == king[0] and ny ==king[1])):
                    nx = nx + dirForward[dir1][2][0]
                    ny = ny + dirForward[dir1][2][1]
                    if(-1<nx<10 and -1<ny<9 and visited[ny][nx] == -1):
                        visited[ny][nx] = visited[y][x] + 1
                        toVisit.append([nx,ny])
    print(-1)
shang = list(map(int,input().split()))
king = list(map(int,input().split()))

bfs(shang,king)


