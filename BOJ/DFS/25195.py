import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
def dfs(now):
    global info
    global check
    if(check[now]):
        return
    else:
        if(info[now]):
            for i in info[now]:
                dfs(i)
        else:
            global answer
            answer = "yes"
            return
n,m = map(int,input().split())
info = [[] for _ in range(n+1)]

for i in range(m):
    s,e = map(int,input().split())
    info[s].append(e)


answer = 'Yes'
check = [0 for _ in range(n+1)]
c = int(input())
tmp = list(map(int,input().split()))
for i in tmp:
    check[i] = 1


dfs(1)
print(answer)
