from collections import deque
from itertools import combinations
import sys
import copy

forwardDir = [[-1,0],[0,-1],[1,0],[0,1]]
    
n,k= map(int,input().split())
info = []
infoAs = [0b00 for _ in range(n)]
ans = 0
arr = [0 for _ in range(26)]
combinationArr = []
numberInit = 0b00
for i in range(26):
    arr[i] = i

for i in (['a','c','n','t','i']):
    arr[ord(i) - ord('a')] = -1
    numberInit = numberInit | (0b01 << (ord(i) - ord('a')))


for i in arr:
    if(i != -1):
        combinationArr.append(i)

for i in range(n):
    info.append(str(input()))
    for j in info[i]:
        infoAs[i] = infoAs[i] | (0b01 << (ord(j) - ord('a')))

if(k<5):
    print(0)
    sys.exit()


for comb in combinations(combinationArr,k-5):
    number = numberInit
    count = 0
    for c in comb:
        number = number | 0b01 << c
    for stri in infoAs:
        if(stri == stri & number):
            count += 1
    ans = max(count,ans)
print(ans)
