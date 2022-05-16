import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def dfs(target,val):
    global info
    global visited
    global answer
    if(info[val] == target):
        answer[target] = 1
        return 
    if(not visited[info[val]]):    
        visited[info[val]] = 1
        dfs(target,info[val])

n = int(input())
info = [0]
answer = [0 for _ in range(n+1)]
for i in range(n):
    info.append(int(input()))

for i in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    visited[i] = 1
    dfs(i,i)

print(sum(answer))
for i in range(1,n+1):
    if(answer[i]):
        print(i)







