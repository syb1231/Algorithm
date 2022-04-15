import sys
import math
from collections import deque
import heapq
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
a = []
b = []
c = []
d = []
check = {}
answer = 0
for i in range(n):
    tmp = list(map(int,input().split()))
    a.append(tmp[0])
    b.append(tmp[1])
    c.append(tmp[2])
    d.append(tmp[3])

for i in range(n):
    for j in range(n):
        sumAB = a[i]+ b[j]
        if(check.get(sumAB)):
            check[sumAB] += 1
        else:
            check[sumAB] = 1

for i in range(n):
    for j in range(n):
        sumCD = -(c[i] + d[j])
        if(check.get(sumCD)):
            answer += check[sumCD]
    
print(answer)
