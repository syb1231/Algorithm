from collections import deque
import sys
sys.setrecursionlimit(100000)

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())

parent = [0 for _ in range(N+1)]
for i in range(1, N + 1):
    parent[i] = i

for i in range(N):
    info = list(map(int,input().split()))
    for j in range(N):
        if(info[j]):
            union_parent(parent,i+1,j+1)
cityToGo = list(map(int,input().split()))

for i in range (1,len(cityToGo)):
    if(find_parent(parent,cityToGo[i]) != find_parent(parent,cityToGo[i-1])):
        print('NO')
        exit()
print('YES')

        
