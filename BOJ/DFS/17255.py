import sys
from collections import deque
import heapq
input = sys.stdin.readline
check ={}
answer = 0

def dfs(sumN,targetN):
    global check
    global answer
    if(targetN == ""):
        if(not check.get(sumN)):

            check[sumN] = 1
            answer +=1
        return

    dfs(sumN+targetN[1:],targetN[1:])
    dfs(sumN+targetN[:-1],targetN[:-1])




targetCount = 0
n  = str(input()[:-1])
for i in range(len(n)):
    targetCount += i


dfs("",n)
print(answer)
