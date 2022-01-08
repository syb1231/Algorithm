from collections import deque
import sys
dq = deque()
                
def bfs():
    while(dq):
        subin = dq.popleft()
        if(subin == K):
             return load[subin] - 1
        if(subin + 1 < 1000001 and load[subin+1] == 0):
            dq.append(subin+1)
            load[subin+1] = load[subin] +1
        if(subin - 1 > -1 and load[subin-1] == 0):
            dq.append(subin-1)
            load[subin-1] = load[subin] +1
        if(subin * 2 < 1000001 and load[subin*2] == 0):
            dq.append(subin*2)
            load[subin*2] = load[subin] +1    
              
N,K = map(int, input().split())
load = [0 for _ in range(1000001)]
load[N] = 1
dq.append(N)
print(bfs())


