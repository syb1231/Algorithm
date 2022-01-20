from collections import deque
import sys
import copy
input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [-1,0,1,0]
ans = 0
def bfs(time):
    maxDist = 1
    maxIndex = 0
    for index in range(N):
        dist = 1
        if(not zari[index]):
            while(dist < N):        
                left = index - dist
                right = index + dist
                dist += 1
                if(left>-1 and zari[left]):
                    if(dist > maxDist):
                        maxDist = dist
                        maxIndex = index
                    break
                if(right<N and zari[right]):
                    if(dist > maxDist):
                        maxDist = dist
                        maxIndex = index
                    break           
    return maxIndex,maxDist

def cal(P):
    global ans
    time = 900
    while(time<2060):
        if(time%100 == 60):
            time = int(time/100) * 100 + 100
        while(outTime[time]):
            humanCheckout = outTime[time].pop()
            if(inOutSame[humanCheckout]):
                inTime[time].pop()
                continue
            humanSeat = human[humanCheckout]
            human[humanCheckout] = 0
            zari[humanSeat] = 0
        while(inTime[time]):
            humanCheckin = (inTime[time].pop())[0]
            nextSeat,ddd = bfs(time)
            human[humanCheckin] = nextSeat
            zari[nextSeat] = humanCheckin
        if(not zari[P]):
            ans += 1
        time += 1

N,T,P = map(int,input().split())
inTime = [[] for _ in range(2101)]
outTime = [[] for i in range(2101)]
inOutSame = [0 for i in range(T+1)] 
zari = [0 for i in range(N)] # 0 ~ N-1 좌석 번호
human = [0 for i in range(T+1)] # 1 ~ N 사람 번호
P -= 1
for i in range(1,T+1):
    tmp1,tmp2 = map(int,input().split())
    inTime[tmp1].append([i,tmp2-tmp1])
    if(tmp1 == tmp2):
        inOutSame[i] = 1
    outTime[tmp2].append(i)
for i in range(900,2101):
    inTime[i].sort(key=lambda x:-x[1])
cal(P)
print(ans)
