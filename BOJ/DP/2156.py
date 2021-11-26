import sys

n = int(sys.stdin.readline())

arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = int(sys.stdin.readline())

dp = []

dp.append(arr[0])
if n>1 : 
    dp.append(arr[0]+arr[1])
if n>2 : 
    dp.append(max(arr[0]+arr[1],arr[0]+arr[2],arr[1]+arr[2]))
for i in range (3,n):
    dp.append(max(dp[i-1],dp[i-2]+arr[i],dp[i-3]+arr[i]+arr[i-1]))

print(dp[n-1])


