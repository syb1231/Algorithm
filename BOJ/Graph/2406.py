import sys
import itertools
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def find(target):
    if target == parent[target]:
        return target
 
    # 경로 압축 최적화
    parent[target] = find(parent[target])
    return parent[target]
 
# union 연산
def union(a, b):
    a = find(a)
    b = find(b)
 
    # 작은 루트 노드를 기준으로 합침
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
 

n,m = map(int,input().split())
parent = [0 for _ in range(n+1)]
for i in range(1,n):
    parent[i] = i
count = 0
for i in range(m):
    x,y = map(int,input().split())
    if(x == 1 or y == 1):
        continue
    if(find(x) != find(y)):
        union(x,y)
        count += 1

info = []
tmp2 = list(map(int,input().split()))
for i in range(n-1):
    tmp = list(map(int,input().split()))
    for j in range(1,n):
        if(i+2 != j+1):
            info.append([i+2,j+1,tmp[j]])


targetCount = n-2
info.sort(key=lambda x:-x[2])
answerCost = 0
answerInfo = []
while(targetCount != count):
    x,y,cost = info.pop()
    if(find(x) != find(y)):
        union(x,y)
        answerCost += cost
        answerInfo.append([x,y])
        count += 1



print(answerCost,end=" ")
print(len(answerInfo))
for i in range(len(answerInfo)):
    print(answerInfo[i][0],answerInfo[i][1])



