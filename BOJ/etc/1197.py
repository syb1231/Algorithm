import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

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

v,e = map(int,input().split())
info = []
parent = [0 for _ in range(v+1)]
for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    tmp = list(map(int,input().split()))
    info.append([tmp[2],tmp[0],tmp[1]])

info.sort(key=lambda x:x[0])
answer = 0
for i in range(len(info)):
    if(find(info[i][1]) != find(info[i][2])):
        union(info[i][1],info[i][2])
        answer += info[i][0]

print(answer)
