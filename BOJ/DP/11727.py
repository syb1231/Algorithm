import sys

n = int(sys.stdin.readline())

dp = []

dp.append(1)

if n>1 : dp.append(3)

for i in range(2,n):
    dp.append(dp[i-1] + dp[i-2] * 2)

print(dp[n-1] % 10007)



