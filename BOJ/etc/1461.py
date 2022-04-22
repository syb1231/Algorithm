import sys
from collections import deque
import heapq
input = sys.stdin.readline
n,m = map(int,input().split())
info = list(map(int,input().split()))

heapMin = []
heapMax = []
answer = 0
for i in info:
    if(i<0):
        heapq.heappush(heapMin,i)
    if(i>0):
        heapq.heappush(heapMax,(-i,i))
answer = -max(max(info),abs(min(info)))

while(heapMin):
    val = heapq.heappop(heapMin)
    count = 1
    while(count < m and heapMin and heapq.heappop(heapMin)):
        count += 1
    answer += abs(val) * 2


while(heapMax):
    val = heapq.heappop(heapMax)[1]
    count = 1
    while(count < m and heapMax and heapq.heappop(heapMax)[1]):
        count += 1
    answer += val * 2

print(answer)
