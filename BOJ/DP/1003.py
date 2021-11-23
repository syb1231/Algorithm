import sys

T = int(sys.stdin.readline())
testCase = [0 for _ in range (T)]
maxNumber = -1
for i in range (T):
    testCase[i]=int(sys.stdin.readline())
    if(maxNumber < testCase[i]) :
        maxNumber = testCase[i]

dp = [[0]*2 for _ in range(maxNumber+1)]
dp[0] = [1,0]
dp[1] = [0,1]


for i in range (2,maxNumber+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in range (T):
    index = testCase[i]
    print(dp[index][0],end=' ')
    print(dp[index][1])
