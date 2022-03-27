import sys
import math
from collections import deque
input = sys.stdin.readline

n,c = map(int,input().split())
homes = []
for i in range(n):
    homes.append(int(input()))

homes.sort()
start = 0
end = 1000000000
answer = 0

while(start<end):
    prev = 0
    mid = (start+end) // 2 
    count = c-1
    for l in range(prev+1,len(homes)):
        distance = homes[l] - homes[prev]
        if(distance>=mid):
            count -= 1
            prev = l
            if(not count):
                break
    if(not count):
        start = mid + 1
        answer = max(mid,answer)
    else:
        end = mid
