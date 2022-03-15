import sys
from collections import deque
input = sys.stdin.readline

def dfs(ans,maxA,maxB,maxC):
    vistied = [[[0 for _ in range(201)] for _ in range(201)] for _ in range(201)]
    toVisit = deque()
    toVisit.append([0,0,maxC])
    vistied[0][0][maxC] = 1
    while(toVisit):
        a,b,c = toVisit.popleft()
        if(a):
            aCopy = a
            bCopy = b
            maximunToFullB = maxB - bCopy  
            if(aCopy>maximunToFullB):
                bCopy = maxB
                aCopy -= maximunToFullB
            else:
                bCopy += aCopy
                aCopy = 0
            if(not vistied[aCopy][bCopy][c]):
                vistied[aCopy][bCopy][c] = 1
                toVisit.append([aCopy,bCopy,c])
            aCopy = a
            cCopy = c
            maximunToFullC = maxC - cCopy
            if(aCopy>maximunToFullC):
                cCopy = maxC
                aCopy -= maximunToFullC
            else:
                cCopy += aCopy
                aCopy = 0
            if(not vistied[aCopy][b][cCopy]):
                vistied[aCopy][b][cCopy] = 1
                toVisit.append([aCopy,b,cCopy])
        else:
            ans[c] = 1
        if(b):
            aCopy = a
            bCopy = b
            maximunToFullA = maxA - aCopy
            if(bCopy>maximunToFullA):
                aCopy = maxA
                bCopy -= maximunToFullA
            else:
                aCopy += bCopy
                bCopy = 0
            if(not vistied[aCopy][bCopy][c]):
                vistied[aCopy][bCopy][c] = 1
                toVisit.append([aCopy,bCopy,c])
                
            bCopy = b
            cCopy = c
            maximunToFullC = maxC - cCopy
            if(bCopy>maximunToFullC):
                cCopy = maxC
                bCopy -= maximunToFullC
            else:
                cCopy += bCopy
                bCopy = 0
            if(not vistied[a][bCopy][cCopy]):
                vistied[a][bCopy][cCopy] = 1
                toVisit.append([a,bCopy,cCopy])    
        if(c):
            aCopy = a
            cCopy = c
            maximunToFullA = maxA - aCopy
            if(cCopy>maximunToFullA):
                aCopy = maxA
                cCopy -= maximunToFullA
            else:
                aCopy += cCopy
                cCopy = 0
            if(not vistied[aCopy][b][cCopy]):
                vistied[aCopy][b][cCopy] = 1
                toVisit.append([aCopy,b,cCopy])

            bCopy = b
            cCopy = c
            maximunToFullB = maxB - bCopy
            if(cCopy>maximunToFullB):
                bCopy = maxB
                cCopy -= maximunToFullB
            else:
                bCopy += cCopy
                cCopy = 0
            if(not vistied[a][bCopy][cCopy]):
                vistied[a][bCopy][cCopy] = 1
                toVisit.append([a,bCopy,cCopy])

maxA,maxB,maxC = map(int,input().split())
ans = [0 for _ in range(201)]
dfs(ans,maxA,maxB,maxC)
for i in range(201):
    if(ans[i]):
        print(i,end=" ")



