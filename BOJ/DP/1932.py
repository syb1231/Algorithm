import sys

n = int(sys.stdin.readline())

arr = [[0]*n for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

# dp = [[0]*2 for _ in range(n)]
# dp[0] = [arr[0][0], arr[0][0]]

for sero in range(1,n): 
    for garo in range(len(arr[sero])):
         if garo == 0 : 
             arr[sero][garo] += (arr[sero-1][garo]) 
         elif garo == sero: 
             arr[sero][garo] +=(arr[sero-1][garo-1]) 
         else : 
             arr[sero][garo] += max(arr[sero-1][garo], arr[sero-1][garo-1])


print(max(arr[n-1]))
