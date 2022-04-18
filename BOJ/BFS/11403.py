import sys
from collections import deque
input = sys.stdin.readline

def bfs(start,end,n,info):
    visited = [0 for _ in range(n)]
    toVisit = deque() 
    toVisit.append(start)

    while(toVisit):
        node = toVisit.popleft()
        if(node == end and visited[end]):
            return 1
        for i in info[node]:
            if(not visited[i]):
                answer[start][i] = 1
                toVisit.append(i)
                visited[i] = 1

    return 0 
                
    
    
n = int(input()) 
info = [[] for _ in range(n)]
answer = [[-1] * n for _ in range(n)]
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if(tmp[j]):
            info[i].append(j)

for i in range(n):
    for j in range(n):
        if(answer[i][j] == -1):
            answer[i][j] = bfs(i,j,n,info)

for i in range(n):
    for j in range(n):
        print(answer[i][j],end=" ")
    print("")
