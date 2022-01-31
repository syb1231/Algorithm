from collections import deque
from itertools import combinations
import sys
import copy

forwardDir = [[-1,0],[0,-1],[1,0],[0,1]]
    
def bfs():
    visited = [-1 for _ in range(1000001)]
    route = [-1 for _ in range(1000001)]
    toVisit = deque()
    toVisit.append(n)
    visited[n] = 0
    maxNumber = 1000001
    while(toVisit):
        now = toVisit.popleft()

        if(now == k):
            print(visited[now])
            count = visited[now]
            ans = deque()
            ans.append(now)
            tmp = now
            for i in range(count):
                tmp = route[tmp]
                ans.append(tmp)
            while(ans):
                print(ans.pop(),end=" ")

        if(now > 0 and visited[now-1] == -1):
            toVisit.append(now-1)
            route[now-1] = now
            visited[now-1] = visited[now]+1
        if(now +1 < maxNumber and visited[now+1] == -1):
            toVisit.append(now+1)
            route[now+1] = now
            visited[now+1] = visited[now]+1
        if(now*2 < maxNumber and visited[now*2] == -1):
            toVisit.append(now*2)
            visited[now*2] = visited[now]+1
            route[now*2] = now


n,k= map(int,input().split())
bfs()
