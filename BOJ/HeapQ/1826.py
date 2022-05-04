import sys
from collections import deque
import heapq
input = sys.stdin.readline

n = int(input())
info = []
hq = []
for i in range(n):
    info.append(list(map(int,input().split())))
end,leftOil = map(int,input().split())
ans = 0
info.sort(key=lambda x:-x[0])
while(leftOil<end):
    if(not info and not hq):
        print(-1)
        exit()
    while(info and info[-1][0]<=leftOil):
        val = info.pop()[1]
        heapq.heappush(hq,(-val,val))
    if(hq):
        leftOil += heapq.heappop(hq)[1]
    else:
        print(-1)
        exit()
    ans += 1
    

print(ans)
