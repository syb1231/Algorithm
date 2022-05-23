import sys
import itertools
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)
dirF = []
dirF.append([[-1,0],[0,-1]])
dirF.append([[1,0],[0,-1]])
dirF.append([[-1,0],[0,1]])
dirF.append([[1,0],[0,1]])
def dfs(x,y,cost):
    global info
    global visited

    if(y == n):
        global answer 
        if(answer<cost):
            answer = cost
        return 
    if(not visited[y][x]):
        for i in range(4):
            isPossible = True
            for d in dirF[i]:
                nx = x + d[0]
                ny = y + d[1]

                if(nx<0 or nx>m-1 or ny<0 or ny>n-1):
                    isPossible = False
                    break
                if(visited[ny][nx]):
                    isPossible = False
                    break

            if(isPossible):
                visited[y][x] = 1
                val = 0
                for d in dirF[i]:
                    nx = x + d[0]
                    ny = y + d[1]                
                    visited[ny][nx] = 1
                    val += info[ny][nx]
                if(x == m-1):
                    dfs(0,y+1,cost+info[y][x]*2+val)
                else:
                    dfs(x+1,y,cost+info[y][x]*2+val)
                visited[y][x] = 0
                for d in dirF[i]:            
                    visited[y + d[1]][ x + d[0]] = 0

    if(x == m-1):
        dfs(0,y+1,cost)
    else:
        dfs(x+1,y,cost)           

            
            


    

n,m = map(int,input().split())
info = []
for i in range(n):
    info.append(list(map(int,input().split())))

if(n<2 or m<2):
    print(0)
    exit()
answer = 0 
visited = [[0 for _ in range(m)] for _ in range(n)]
dfs(0,0,0)
print(answer)
