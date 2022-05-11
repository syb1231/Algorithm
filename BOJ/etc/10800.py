import sys
from collections import deque
import heapq
input = sys.stdin.readline

n = int(input())
info = []
for i in range(n):
    tmp1,tmp2 = map(int,input().split())
    info.append([tmp1,tmp2,i])

ans = [-1 for _ in range(n)]
check = {}
info.sort(key=lambda x:x[1])
maxSize = info[0][1]
res = 0
val = 0
for i in range(n):
    c,s,index=info[i]

    if(maxSize<s):
        maxSize = s
        val = 0
    if(check.get(c)):
        if(check[c][0] < s):
            check[c][0] = s
            ans[index] = res - check[c][2] - val
            check[c][1] = s
        else:
            ans[index] = res - check[c][2] - val + check[c][1]
            check[c][1] += s
        check[c][2] += s    
        
    else:
        check[c] = [s,s,s]
        ans[index] = res - val

    res += s   
    val += s

for i in range(n):
    print(ans[i])
