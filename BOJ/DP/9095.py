import sys 

T = int(sys.stdin.readline())
testCase = [0 for _ in range (T)]
maxNumber = -1
for i in range (T):
    testCase[i] = int(sys.stdin.readline())
    if maxNumber<testCase[i]:
        maxNumber = testCase[i]

dp = [0 for _ in range (maxNumber+1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,maxNumber+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range (T):
    index = testCase[i]
    print(dp[index])

