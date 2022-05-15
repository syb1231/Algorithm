import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
info = list(map(int,input().split()))
info.sort()
disInfo = []

for i in range(1,n):
    disInfo.append(info[i] - info[i-1])

disInfo.sort(reverse = True)
ans = 0
for i in range(k-1,n-1):
    ans += disInfo[i]
print(ans)
