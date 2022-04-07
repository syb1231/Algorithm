import sys
import math
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def bfs(start,end):
    visited = [-1 for _ in range(N+1)]
    toVisit = deque()
    toVisit.append([start,0])
    visited[start] = start
    answer = 0
    while(toVisit):
        now,count = toVisit.popleft()
        if(now == end):
            answer += count
            break
        for nextNode in info[now]:
            if(visited[nextNode] == -1):
                visited[nextNode] = now
                toVisit.append([nextNode,count+1])
    toVisit = deque()
    toVisit.append(end)
    point = visited[end]
    newVisited = [0 for _ in range(N+1)]
    while(visited[point] != point):
        newVisited[point] = 1
        point = visited[point]

    while(toVisit):
        now = toVisit.popleft()
        if(now == start):
            answer += newVisited[now]
            return answer
        for nextNode in info[now]:
            if(not newVisited[nextNode]):
                newVisited[nextNode] = newVisited[now] + 1
                toVisit.append(nextNode)  
    return answer

N,M = map(int,input().split())
info = [[] for _ in range(N+1)]
for i in range(M):
    start,end = map(int,input().split())
    info[start].append(end)
    info[end].append(start)

for i in range(N+1):
    info[i].sort()

start,end = map(int,input().split())

print(bfs(start,end))

# 대가리 박지 말고 펜으로 제대로 쓰고 하자
# 문제 똑바로 읽자 제발
