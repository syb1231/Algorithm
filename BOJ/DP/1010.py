import sys

T = int(sys.stdin.readline())

NM = [[0]*2 for i in range(T)]

for i in range(T):
    arr= list(map(int, input().split()))
    NM[i] = arr

ans = 0
for i in range(T):
    N = NM[i][0]
    M = NM[i][1]
    ans = 1
    for i in range(N):
        ans *= M-i
        ans /= i+1
    print(int(ans))
