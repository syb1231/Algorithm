import sys

n = int(sys.stdin.readline())

dp = [[0]*2 for _ in range(n)]

dp[0] = [0,1]
if n>1 : dp[1] = [1,0]
if n>2 : dp[2] = [1,1]
for i in range(2,n):
    dp[i][0] = dp[i-2][0] * 2 + dp[i-2][1]
    dp[i][1] = dp[i-2][1] + dp[i-2][0]

print(dp[n-1][1]+dp[n-1][0])



