from collections import deque
import sys
import copy
sys.setrecursionlimit(250000)
dx = [-1,0,1,0]
dy = [0,-1,0,1]
maxNumber = 0
    


def dfs(dir,info_o,count):
    global maxNumber
    
    if(count == 6): # 종료 조건
        number = max(map(max, info_o))
        if(maxNumber < number):
            maxNumber = number
        return

    if(max(map(max, info_o)) < maxNumber>>5-count): # 백트래킹
        return

    info = copy.deepcopy(info_o)
    now = [[0]*N for _ in range(N)]
    if(dir == 0):
        for y in range(N):
            for x in range(N):
                if(info[y][x]):

                    bx = x - dx[dir]
                    by = y - dy[dir]

                    while(-1<bx<N and -1<by<N):
                        if(info[by][bx]):
                            if(info[by][bx] == info[y][x]):
                                info[by][bx] = 0
                                info[y][x] = 2 * info[y][x] 
                            break 
                        bx = bx - dx[dir]
                        by = by - dy[dir]

                    nx = x + dx[dir]
                    ny = y + dy[dir]
        
                    while(-1<nx<N and -1<ny<N and not now[ny][nx]):
                        nx = nx + dx[dir]
                        ny = ny + dy[dir]
                    now[ny-dy[dir]][nx-dx[dir]] = info[y][x]  
        for n_dir in range(4):
            dfs(n_dir,now,count+1) 
    if(dir == 1):
        for x in range(N):
            for y in range(N):
                if(info[y][x]):
                    bx = x - dx[dir]
                    by = y - dy[dir]
                    while(-1<bx<N and -1<by<N):
                        if(info[by][bx]):
                            if(info[by][bx] == info[y][x]):
                                info[by][bx] = 0
                                info[y][x] = 2 * info[y][x] 
                            break 
                        bx = bx - dx[dir]
                        by = by - dy[dir]
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    while(-1<nx<N and -1<ny<N and not now[ny][nx]):
                        nx = nx + dx[dir]
                        ny = ny + dy[dir]
                    now[ny-dy[dir]][nx-dx[dir]] = info[y][x]   
        for n_dir in range(4):
            dfs(n_dir,now,count+1) 
    if(dir == 2):
        for y in range(N):
            for x in range(N-1,-1,-1):
                if(info[y][x]):
                    bx = x - dx[dir]
                    by = y - dy[dir]
                    while(-1<bx<N and -1<by<N):
                        if(info[by][bx]):
                            if(info[by][bx] == info[y][x]):
                                info[by][bx] = 0
                                info[y][x] = 2 * info[y][x] 
                            break 
                        bx = bx - dx[dir]
                        by = by - dy[dir]
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    while(-1<nx<N and -1<ny<N and not now[ny][nx]):
                        nx = nx + dx[dir]
                        ny = ny + dy[dir]
                    now[ny-dy[dir]][nx-dx[dir]] = info[y][x]   
        for n_dir in range(4):
            dfs(n_dir,now,count+1) 
    if(dir == 3):
        for x in range(N):
            for y in range(N-1,-1,-1):
                if(info[y][x]):
                    bx = x - dx[dir]
                    by = y - dy[dir]
                    while(-1<bx<N and -1<by<N):
                        if(info[by][bx]):
                            if(info[by][bx] == info[y][x]):
                                info[by][bx] = 0
                                info[y][x] = 2 * info[y][x] 
                            break 
                        bx = bx - dx[dir]
                        by = by - dy[dir]
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    while(-1<nx<N and -1<ny<N and not now[ny][nx]):
                        nx = nx + dx[dir]
                        ny = ny + dy[dir]
                    now[ny-dy[dir]][nx-dx[dir]] = info[y][x]   
        for n_dir in range(4):
            dfs(n_dir,now,count+1) 

N = int(sys.stdin.readline())
info_o = []
for i in range(N):
    info_o.append(list(map(int,input().split())))
for dir in range(4):
    dfs(dir,info_o,1)
print(maxNumber)
