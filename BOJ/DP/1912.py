import sys

n = int(sys.stdin.readline())

#arr = [[0]*n for _ in range(n)]

arr= list(map(int, input().split()))
dp=[]
dp.append(arr[0])

for i in range (n-1):
    dp.append(max(dp[i]+arr[i+1],arr[i+1]))

print(max(dp))
