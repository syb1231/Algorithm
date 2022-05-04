import sys
from collections import deque
input = sys.stdin.readline
dirFowrard = [[0,0],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
dirFowrard2 = [[-1,-1],[-1,1],[1,-1],[1,1]]
n,m = map(int,input().split())
info = []
magicInfo = []
xy = deque()
check = [[0 for _ in range(n)] for _ in range(n)]
answer = 0

for i in range(n):
    info.append(list(map(int,input().split())))

for i in range(m):
    magicInfo.append(list(map(int,input().split())))

xy.append([0,n-1])
xy.append([1,n-1])
xy.append([0,n-2])
xy.append([1,n-2])
for d,s in magicInfo:
    plus = []
    # 1
    for i in range(len(xy)):
        x,y = xy.popleft()
        x += dirFowrard[d][0]*s
        y += dirFowrard[d][1]*s
        if(x>=0):
            x = x % n
        else:
            while(x<0):
                x = n + x
        if(y>=0):
            y = y % n
        else:
            while(y<0):
                y = n + y
        # 2
        info[y][x] += 1
        xy.append([x,y])
    # 4
    for i in range(len(xy)):
        x,y = xy.popleft()
        val = 0
        check[y][x] = 1
        for dir2 in range(4):
            nx = x + dirFowrard2[dir2][0]
            ny = y + dirFowrard2[dir2][1]
            if(-1<nx<n and -1<ny<n and info[ny][nx]):
                val += 1

        plus.append([x,y,val])

    for i in range(len(plus)):
        x,y,val = plus.pop()
        info[y][x] += val
    for y in range(n):
        for x in range(n):
            if(info[y][x] > 1 and not check[y][x]):
                info[y][x] -= 2
                xy.append([x,y])

            check[y][x] = 0
            
ans = 0
for y in range(n):
    for x in range(n):
        ans += info[y][x]

print(ans)




#

   

