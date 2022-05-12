import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
dirFoward = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1],[1,1],[-1,1]]
n = int(input())
info = [[] for _ in range(n)]
tmp = list(map(int,input().split()))
for i in range(n):
    info[i] = [i,tmp[i]]
infoAns = []
check = {}
for c in (list(combinations(info,2))):
    val = c[0][1] + c[1][1]
    infoAns.append(val)
    if(check.get(val)):
        check[val].append([c[0][0],c[1][0]])
    else:
        check[val] = [[c[0][0],c[1][0]]]

infoAns.sort()
ans = float('inf')
for i in range(1,len(infoAns)):
    val = infoAns[i] -infoAns[i-1]
    if(val<ans):
        isFinish = False
        for c in check[infoAns[i]]:
            t1 = c[0]
            t2 = c[1]
            for cs in check[infoAns[i-1]]:
                if(t1 == cs[0] or t1 == cs[1] or t2 == cs[0] or t2 == cs[1]):
                    continue
                else:
                    ans = val
                    isFinish = True
                    break
                if(isFinish):
                    break
print(ans)
