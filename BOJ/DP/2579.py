import sys

stairsMax = int(sys.stdin.readline())
stairs = [0 for _ in range(stairsMax+1
                           
for i in range(1,stairsMax+1):
    stairs[i] = int(sys.stdin.readline())
                           
dp = [[0]*2 for _ in range(stairsMax+1)]
dp[1] = [stairs[1],stairs[1]]
                           
if(stairsMax > 1) :
    dp[2][0] = stairs[2]
    dp[2][1] = stairs[1] + stairs[2]
                           
if(stairsMax > 2) :
    #minStair = min (stairs[0], stairs[1], stairs[2])
    dp[3][0] = stairs[1] + stairs[3]
    dp[3][1] = stairs[2] + stairs[3] 

for i in range (4,stairsMax+1):
    #minStair = min (stairs[i-2], stairs[i-1])
    dp[i][0] =max(dp[i-2][0], dp[i-2][1]) + stairs[i] 
    dp[i][1] = dp[i-1][0] + stairs[i]
    
print(max(dp[stairsMax][0],dp[stairsMax][1]))
