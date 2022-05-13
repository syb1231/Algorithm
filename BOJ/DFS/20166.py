import sys 
input=sys.stdin.readline
dirX = [-1,1,0,0,-1,-1,1,1]
dirY = [0,0,-1,1,1,-1,1,-1]

def dfs(x,y,count,strTmp):
    global info
    global check
    if(count == 6):
        return 
    if(check.get(strTmp)):
        global ans
        ans[strTmp] += check[strTmp]

    for dirF in range(8):
        nx = x + dirX[dirF]
        ny = y + dirY[dirF]
        if(nx == -1):
            nx = m-1
        elif(nx == m):
            nx = 0
        
        if(ny == -1):
            ny = n-1
        elif(ny == n):
            ny = 0

        dfs(nx,ny,count+1,strTmp+info[ny][nx])
    
    


n,m,k = map(int,input().split())
check = {}
ans = {}
val = 0
info = [list(input().strip()) for _ in range(n)]
for i in range(k):
    tmp = input()[:-1]
    if(check.get(tmp)):
        check[tmp] += 1
    else:
        check[tmp] = 1
        ans[tmp] = 0

for y in range(n):
    for x in range(m):
        dfs(x,y,1,info[y][x])

for a in ans:
    print(ans[a])
