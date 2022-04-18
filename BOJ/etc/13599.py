import sys
from collections import deque
input = sys.stdin.readline
dirFoward = [[-1,0],[1,0],[0,-1],[0,1]]

n,m = map(int,input().split())
info = []
for i in range(n):
    info.append(str(input()))
check = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        for dir1 in dirFoward:
            nx = x + dir1[0]
            ny = y + dir1[1]
            if(-1<nx<m and -1<ny<n):
                if(info[y][x] != info[ny][nx]):
                    check[y][x] = 1
                    break

res = 0
for y in range(n):
    for x in range(m):
        res += check[y][x] 
print((2**(m*n-res)) % (10**9 + 7))
        
