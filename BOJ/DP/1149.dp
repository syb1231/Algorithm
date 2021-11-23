import sys

N = int(sys.stdin.readline())
homeCost = [[0]*3 for _ in range (N+1)]
dp = [[0]*3 for _ in range (N+1)]

for i in range (1,N+1):
    homeCost[i][0],homeCost[i][1],homeCost[i][2] = map(int, sys.stdin.readline().split()) 

dp[0][0] = homeCost[0][0]
dp[0][1] = homeCost[0][1]
dp[0][2] = homeCost[0][2]

for i in range (1,N+1):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + homeCost[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + homeCost[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + homeCost[i][2]

print(min(dp[N][0], dp[N][1], dp[N][2]))
