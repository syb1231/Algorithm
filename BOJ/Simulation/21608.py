import sys
from collections import deque
import heapq
input = sys.stdin.readline
forwardDir = [[-1,0],[1,0],[0,1],[0,-1]]

def cal(nowHumanIndex,humanLike,humanInfo,info):
    possibleSit = [[0 for _ in range(n)] for _ in range(n)]
    maxVal = 0
    humanIndex = humanLike[nowHumanIndex][0]
    for person in ((humanLike[nowHumanIndex])[1:]):
        if(humanInfo[person]):
            for dir1 in range(4):
                nx = humanInfo[person][0] + forwardDir[dir1][0]
                ny = humanInfo[person][1] + forwardDir[dir1][1]
                if(-1<nx<n and -1<ny<n and not info[ny][nx]):
                    possibleSit[ny][nx] += 1
    
    for y in range(n):
        for x in range(n):
            maxVal = max(maxVal,possibleSit[y][x])
    maxLeftSit = 0
   
    for y in range(n):
        for x in range(n):
            if(possibleSit[y][x] == maxVal and not info[y][x]):
                possibleSit[y][x] = 1
                for dir1 in range(4):
                    nx = x + forwardDir[dir1][0]
                    ny = y + forwardDir[dir1][1]
                    if(-1<nx<n and -1<ny<n and not info[ny][nx]):
                        possibleSit[y][x] += 1
            else:
                possibleSit[y][x] = 0

    for y in range(n):
        for x in range(n):
            maxLeftSit = max(maxLeftSit,possibleSit[y][x])
    for y in range(n):
        for x in range(n):
            if(possibleSit[y][x] == maxLeftSit and not info[y][x]):
                humanInfo[humanIndex] = [x,y]
                info[y][x] = humanIndex
                return 
    
n = int(input())
humanInfo = [[] for _ in range(n**2+1)]
info =  [[0 for _ in range(n)] for _ in range(n)]
humanLike = []
answer = 0
for i in range(n**2):
    humanLike.append(list(map(int,input().split())))

for i in range(n**2):
    cal(i,humanLike,humanInfo,info)

for i in range(n**2):
    humanIndex = humanLike[i][0]
    x,y = humanInfo[humanIndex] 
    count = 0
    arr = humanLike[i][1:]
    for dir1 in range(4):
        nx = x + forwardDir[dir1][0]
        ny = y + forwardDir[dir1][1]
        if(-1<nx<n and -1<ny<n and info[ny][nx] in arr):
            count += 1  
    if(count == 1):
        answer += 1
    elif(count == 2):
        answer += 10
    elif(count == 3):
        answer += 100
    elif(count == 4):
        answer += 1000
print(answer)
            
    
