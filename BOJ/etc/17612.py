import sys
from collections import deque
import heapq

class node:
    def __init__(self, time,customNum, calNum):
        self.time = time
        self.customNum = customNum
        self.calNum = calNum

    def __lt__(self, other):
        if self.time < other.time:   
            return True
        elif self.time == other.time:
            return self.calNum < other.calNum  
        else:
            return False

    def __str__(self):
        return 'time : {},customNum : {}, calNum : {}'.format(self.time, self.customNum, self.calNum)

class node2:
    def __init__(self, time,customNum, calNum):
        self.time = time
        self.customNum = customNum
        self.calNum = calNum

    def __lt__(self, other):
        if self.time < other.time:   
            return True
        elif self.time == other.time:
            return self.calNum > other.calNum  
        else:
            return False

    def __str__(self):
        return 'time : {},customNum : {}, calNum : {}'.format(self.time, self.customNum, self.calNum)

input = sys.stdin.readline


n,k = map(int,input().split())
info = []
humanInfo = {}
exitOrder = []
calHerb = [[] for _ in range(k)]
calLeftTime = []
for i in range(n):
    info.append(list(map(int,input().split())))
    humanInfo[info[i][0]] =  info[i][1]
for i in range(k):
   heapq.heappush(calLeftTime, node(0,0,i))

for i in range(n):
    cal = heapq.heappop(calLeftTime)
    if(cal.time !=0):
        heapq.heappush(exitOrder, node2(cal.time,cal.customNum,cal.calNum))
    heapq.heappush(calLeftTime, node(cal.time+info[i][1],info[i][0],cal.calNum))

while(calLeftTime):
    cal = heapq.heappop(calLeftTime)
    if(cal.time !=0):
        heapq.heappush(exitOrder, node2(cal.time,cal.customNum,cal.calNum))

multi = 1
answer = 0
while(exitOrder):
    cal = heapq.heappop(exitOrder)
    
    answer += cal.customNum * multi
    multi += 1

print(answer)
