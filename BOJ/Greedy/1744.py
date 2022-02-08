from collections import deque
from itertools import combinations
import sys
import copy
import heapq
input = sys.stdin.readline
pq = []
n = int(input())
arr = [0 for _ in range(n)]
ans = 0
for i in range(n):
    arr[i] = int(input())

arr.sort()
minusIndex = -1
plusIndex = -1
zero = False
point = 0
oneCount = 0
for i in range(len(arr)):
    if(arr[i] < 0):
        minusIndex = i
    elif(arr[i] == 0):
        zero = True
    elif(arr[i] == 1):
        oneCount += 1
    if(arr[i] > 1):
        plusIndex = i
        break

if(minusIndex != -1):
    if(minusIndex % 2):
        while(point < minusIndex):
            ans += arr[point] * arr[point+1]
            point += 2
    else:
        while(point < minusIndex):
            ans += arr[point] * arr[point+1]
            point += 2
        if(zero):
            zero = False
        else:
            ans += arr[point]
index = n-1
ans += oneCount
if(plusIndex != -1):
    while(index >= plusIndex):
        if(index-1 < plusIndex):
            ans += arr[plusIndex]
            break
        else:
            ans += arr[index] * arr[index-1]
            index -= 2

print(ans)

