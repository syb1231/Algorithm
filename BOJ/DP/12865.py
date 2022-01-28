from collections import deque
from itertools import combinations
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n,k = map(int,input().split())
info = []

for i in range(n):
    info.append(list(map(int,input().split())))

d = [[0]*(k+1) for _ in range(n)]
for i in range(1,k+1):
    if(info[0][1]>i):
        continue
    else:
        d[0][i] = info[0][1]

for i in range(n):
    for j in range(1,k+1):
        if(info[i][0] > j):
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(info[i][1] + d[i-1][j-info[i][0]],d[i-1][j])
print(d[n-1][k])
# 초항을 세워서 확인해 보자 점화식 만들기 개 어렵네 
