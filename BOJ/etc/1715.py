import sys
import math
from collections import deque
import heapq
#sys.setrecursionlimit(100000)
input = sys.stdin.readline

info = []
n = int(input())
for i in range(n):
    info.append(int(input()))

info.sort()
answer = 0
while(len(info) > 1):
    tmp1 = heapq.heappop(info)
    tmp2 = heapq.heappop(info)
    tmp3 = tmp1 + tmp2
    answer += tmp3
    heapq.heappush(info,tmp3)

print(answer)
