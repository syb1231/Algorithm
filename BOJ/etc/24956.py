import sys
from collections import deque
import heapq
input = sys.stdin.readline

n = int(input())
info = str(input()[:-1])
eCount = 0
hSum = 0
answer = 0
start = n-1
while(start>-1 and eCount<2):
    if(info[start] == 'E'):
        eCount += 1
    start -= 1

for i in range(start,-1,-1):
    if(info[i] == 'E'):
        eCount += 1
    elif(info[i] == 'H'):
        hSum += (2**eCount - eCount -1) % 1000_000_007
    elif(info[i] == 'W'):
        answer += hSum
        answer = answer % 1000_000_007
print(answer)




