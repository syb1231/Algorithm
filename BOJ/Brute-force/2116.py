import sys
import math
from collections import deque
import heapq
#sys.setrecursionlimit(100000)
input = sys.stdin.readline

target = [1,2,3,4,5,6]
t = [5,3,4,1,2,0]
info = []
otherSideInfo = []
n = int(input())
for i in range(n):
    info.append(list(map(int,input().split())))
    otherSideInfo.append([-1,1,2,3,4,5,6])
    for index in range(6):
        val = info[i][index]
        otherSideInfo[i][val] = info[i][t[index]]

answer = []      
for t in target:
    tmp = 0
    val = t
    for i in range(len(info)):
        nextVal = otherSideInfo[i][val] 
        for plus in [6,5,4,3,2,1]:
            if(plus != val and plus != nextVal):
                tmp += plus
                break    
        val = nextVal
    answer.append(tmp)

print(max(answer))
