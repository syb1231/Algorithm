from collections import deque
from itertools import combinations
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
parent = {}
info = []
ans = 0
count = 0
for i in range(0, n+1):
    parent[i] = i
for i in range(m):
    info.append(list(map(int,input().split())))
info.sort(key=lambda x:x[2])

for i in info:
    if(find(i[0]) != find(i[1])):
        union(i[0],i[1])
        ans += i[2]
        count += 1
        if(count == n-1):
            print(ans)
            exit()
        

