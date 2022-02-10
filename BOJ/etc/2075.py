from collections import deque
from itertools import combinations
import sys
import copy
import heapq
input = sys.stdin.readline
pq = []
n = int(input())
arr = []
for i in range(n):
    arr = list(map(int,input().split()))
    for j in arr:
        heapq.heappush(pq,j)
        if(len(pq)>n):
            heapq.heappop(pq)
    
print(heapq.heappop(pq))
 
