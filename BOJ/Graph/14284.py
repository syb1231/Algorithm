import sys
import heapq
input = sys.stdin.readline


n,m = map(int,input().split())
info = []
infoToCal = [[] for _ in range(n+1)]

for i in range(m):
    tmp = list(map(int,input().split()))
    infoToCal[tmp[0]].append([tmp[1],tmp[2]])
    infoToCal[tmp[1]].append([tmp[0],tmp[2]])

s,t= map(int,input().split())

index = 0

q  = []
heapq.heappush(q,[0,s])
ans = [float('inf') for _ in range(n+1)]
ans[s] = 0

while(q):
    dis,node = heapq.heappop(q)
    if(ans[node] < dis):
        continue
    for n,d in infoToCal[node]:
        newD = dis + d
        if(newD < ans[n]):
            ans[n] = newD
            heapq.heappush(q,[newD,n])
   
print(ans[t])


