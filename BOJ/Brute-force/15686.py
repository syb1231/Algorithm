from collections import deque
from itertools import combinations
import sys
import copy
forwardDir = [[-1,0],[0,-1],[1,0],[0,1]]


n,m = map(int, input().split())
city = [list(map(int, input().split())) for i in range(n)]
chicken = []
house = []
ans = float('inf')

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

for comb in combinations(chicken,m):
    dist = 0
    for x,y in house:
        dist += min([abs(x-c[0]) + abs(y-c[1]) for c in comb])
    if(ans>dist):
        ans = dist
print(ans)
