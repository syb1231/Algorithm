import sys

n = int(sys.stdin.readline())

dp = [[0 for _ in range(10)] for i in range(n)]

for i in range(1,10):
    dp[0][i] = 1

for i in range(1,n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif  j == 9:
            dp[i][j] = dp[i-1][8]
        else :
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
ans = 0
for i in range(10):
    ans += dp[n-1][i]

print(ans % 1000000000)


