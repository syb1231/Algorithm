import sys
from collections import deque
import heapq
input = sys.stdin.readline
n = int(input())
info = []
for i in range(n):
    info.append(int(input()))

s = []
answer = 0
for i in range(n):
    target = info[i]

    while(s and s[-1]<=target):
        s.pop()
    answer  += len(s)
    s.append(target)

print(answer)
