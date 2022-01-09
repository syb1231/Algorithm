from collections import deque
import sys
sys.setrecursionlimit(100000)

def bfs():
    to_visit = deque()
    visited = [0 for i in range(F+1)]
    to_visit.append(S)
    
    while(to_visit):
        now = to_visit.popleft()
        if(now == G):
            return visited[now]
        for forward in (+U,-D):
            if(0<now + forward<F+1 and forward and not visited[now+forward]):
                to_visit.append(now+forward)
                visited[now+forward] = visited[now] + 1

    return "use the stairs"
F,S,G,U,D = map(int,input().split())

print(bfs())
