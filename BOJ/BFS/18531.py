from collections import deque
from itertools import combinations
import sys
import copy
input = sys.stdin.readline
visited = set()
toVisit = deque()
ans = 0 
h = 0
def bfs():
    global h
    global ans
    while(toVisit):
        now,dist  = toVisit.popleft()
        for i in [-1,1]:
            nNow = now + i
            if not (nNow in visited):
                visited.add(nNow)
                toVisit.append([nNow,dist+1])
                h -= 1
                ans += dist
                if(h == 0):
                    print(ans)
                    return


s,h = map(int,input().split())
shelter = list(map(int,input().split()))
for i in shelter:
    toVisit.append([i,1])
    visited.add(i)
bfs()
