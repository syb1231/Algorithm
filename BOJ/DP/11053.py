import sys

N = int(sys.stdin.readline())

arr = list(map(int, input().split()))

dp = [0 for _ in range (N)]

for i in range(N):
    for index in range(i):
        if(arr[index] < arr[i] and dp[index] > dp[i] ) :
            dp[i] = dp[index]       
    dp[i] += 1

print(max(dp))


