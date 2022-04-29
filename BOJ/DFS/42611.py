import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(index,cost):
    global maxCost
    global maxCostIndex

    if(len(info[index]) > 1 or index == startIndex):
        for i in info[index]:
            if(not visited[i[0]]):
                visited[i[0]] = 1
                dfs(i[0],cost+i[1])
                visited[i[0]] = 0
    else:
        if(cost>maxCost):
            maxCost = cost
            maxCostIndex = index


    


n = int(input())
info = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(n-1):
    tmp = list(map(int,input().split()))
    info[tmp[0]].append([tmp[1],tmp[2]])
    info[tmp[1]].append([tmp[0],tmp[2]])

startIndex = 1
visited = [0 for _ in range(n+1)]  
visited[1] = 1
maxCost,maxCostIndex = 0,0
dfs(1,0)

startIndex = maxCostIndex
visited = [0 for _ in range(n+1)]
visited[maxCostIndex] = 1
maxCost = 0
dfs(maxCostIndex,0)

print(maxCost)


