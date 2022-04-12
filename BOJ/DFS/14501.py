import sys
import math
from collections import deque
import heapq
sys.setrecursionlimit(100000)
input = sys.stdin.readline
answer = 0
def dfs(date,cost,n):
    global info
    if(date > n):
        global answer
        answer = max(answer,cost)
        return
    if(date + info[date][0]  > n + 1):
        dfs(date + info[date][0] ,cost,n)
    else:
        dfs(date + info[date][0] , cost + info[date][1],n)
    
    dfs(date+1,cost,n)




n = int(input())
info = [[0,0]]
for i in range(n):
    info.append(list(map(int,input().split())))

#info.sort(key=lambda x:x[1],reverse= True)
#info.sort(key=lambda x:x[0])
dfs(1,0,n)
print(answer)
