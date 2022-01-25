from collections import deque
from itertools import combinations
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def cal(n,info,inDegree,ans):
    dq = deque()
    for i in range(1,n+1):
        if(not inDegree[i]):
            dq.append(i)
    while(dq):
        s = dq.popleft()
        ans.append(s)
        for i in range(len(info[s])):
            inDegree[info[s][i]] -= 1
            if(not inDegree[info[s][i]]):
                dq.append(info[s][i])


n,m = map(int,input().split())
info = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
ans = []
for i in range(m):
    a,b = map(int,input().split())
    inDegree[b] += 1
    info[a].append(b)
cal(n,info,inDegree,ans)
for i in ans:
    print(i,end=' ')
