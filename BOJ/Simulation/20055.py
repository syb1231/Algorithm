import sys
from collections import deque
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
A = deque(list(map(int,input().split())))
isRobot = deque([0]*n)

answer = 0
while(True):
    A.rotate(1)
    isRobot.rotate(1)
    isRobot[-1] = 0
    for i in range(n-2,-1,-1):
        if(isRobot[i] and not isRobot[i+1] and A[i+1]):
            isRobot[i] = 0
            isRobot[i+1] = 1
            A[i+1] -= 1
    isRobot[-1] = 0
    if(not isRobot[0] and A[0]):
        A[0] -= 1
        isRobot[0] = 1
    
    answer += 1
    if(A.count(0)>=k):
        break
print(answer)
