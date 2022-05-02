import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
info = []
for i in range(n):
    info.append(int(input()))

info.sort()

noneData = deque()
leftData = deque()

target = 1
index = 0
answer = 0
maxVal = info[-1]
while(target<=maxVal and index + len(noneData)  < len(info)):
    if(target<info[index]):
        noneData.append(target)
        target += 1
    elif(target>info[index]):
        if(noneData):
            answer += info[index]  - noneData.popleft()
        index += 1
    else:
        target += 1
        index += 1
        
for noneNum in noneData:
    answer += info[index] - noneNum
    index += 1

print(answer)
