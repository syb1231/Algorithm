import sys

T = int(sys.stdin.readline())

testCase = [0 for i in range(T)]

for i in range(T):
    testCase[i] = int(sys.stdin.readline())
dp = []

arr = [0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(len(arr)):
    dp.append(arr[i])

for i in range(11,101):
    dp.append(dp[i-2] + dp[i-3])

for i in range(T):
    print(dp[testCase[i]])


