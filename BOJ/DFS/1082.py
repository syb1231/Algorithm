import sys
input = sys.stdin.readline

answer = '0'
tmp = [0 for _ in range(10)]
def dfs(m,n,tmp):
    if(n == -1):
        global answer
        if(tmp != '' and int(answer) < int(tmp)):
            answer = tmp
        return

    global p
    count = 0
    if(possibleP[n]):
        count = m // p[n]
    for i in range(count+1):
        tmp2 = str(n) * i
        dfs(m-p[n]*i,n-1,tmp+tmp2)
    
        

n = int(input())
p = list(map(int,input().split()))
m = int(input())
check = {}
possibleP = [1 for _ in range(n)]
for i in range(n-1,-1,-1):
    if(check.get(p[i])):
        possibleP[i] = 0
    else:
        check[p[i]] = 1
dfs(m,n-1,"")
print(answer)
