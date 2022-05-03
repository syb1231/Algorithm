import sys
from collections import deque
import heapq
input = sys.stdin.readline
forwardDir = [[-1,0],[1,0],[0,1],[0,-1]]
def bf(info,maxSize):
    global possibleArray
    for y in range(n):
        for x in range(m):
            if(info[y][x] == '#'):
                possibleMax = 0
                maxCount = 1
                while(maxCount <= maxSize): 
                    isPossible = True
                    for dir1  in range(4):
                        nx = x + forwardDir[dir1][0] * maxCount
                        ny = y + forwardDir[dir1][1] * maxCount

                        if(nx<0 or nx>m-1 or ny<0 or ny>n-1 or info[ny][nx] == '.'):
                            isPossible = False
                            break
                    if(isPossible):
                        possibleMax = maxCount
                        maxCount += 1
                    else:
                        break
                possibleArray[y][x] = possibleMax

def bf2(info,maxSize,pointX,pointY,targetVal):
    global answer

    for y in range(n):
        for x in range(m):
            if(info[y][x] == '#' and (abs(pointX-x) + abs(pointY-y))>targetVal):               
                possibleMax = 0
                maxCount = 1

                while(maxCount <= maxSize): 
                    isPossible = True
                    for dir1  in range(4):
                        nx = x + forwardDir[dir1][0] * maxCount
                        ny = y + forwardDir[dir1][1] * maxCount

                        if(nx<0 or nx>m-1 or ny<0 or ny>n-1 or info[ny][nx] == '.' or (abs(pointX-nx) + abs(pointY-ny))<=targetVal):
                            isPossible = False
                            break
    
                    if(isPossible):
                        possibleMax = maxCount
                        maxCount += 1
                    else:
                        break     
                answer = max(answer, (possibleMax*4 + 1)  * (targetVal*4 + 1))          
             
n,m = map(int,input().split())
info = []
for i in range(n):
    info.append(str(input()[:-1]))

maxGaro = m
if(not (maxGaro%2)):
    maxGaro -= 1
maxCount = maxGaro // 2 
possibleArray = [[-1 for _ in range(m)] for _ in range(n)]
answer = 0
bf(info,maxCount)
for y in range(n):
    for x in range(m):
        val = possibleArray[y][x]
        while(val != -1):
            bf2(info,maxCount,x,y,val)
            val -= 1

print(answer)



