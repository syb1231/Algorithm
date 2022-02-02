from collections import deque
from itertools import combinations
import sys
import copy

n,m = map(int,input().split())
memmoryInfo = list(map(int,input().split()))
costInfo = list(map(int,input().split()))
maxIndex = sum(costInfo)+1
d = [[0]*(maxIndex) for _ in range(2)]
ans = float('inf')

for i in range(costInfo[0],maxIndex):
    d[0][i] = memmoryInfo[0]
    if(d[0][i] >= m):
            ans = min(ans,i)


for i in range(1,n):
    index = i%2
    beforeIndex = (i+1)%2 
    for j in range(1,maxIndex):
        if(costInfo[i] > j):
            d[index][j] = d[beforeIndex][j]
        else:
            d[index][j] = max(memmoryInfo[i] + d[beforeIndex][j-costInfo[i]],d[beforeIndex][j])

        if(d[index][j] >= m):
            ans = min(ans,j)

print(ans)

# 초반에 공간 복잡도 고려 안함
# 시간 복잡도 고려 안해서 한번 더 터짐
