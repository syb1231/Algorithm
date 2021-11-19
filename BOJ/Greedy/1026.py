import sys

S = int(sys.stdin.readline()) 

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=False)

sum = 0
for i in range(S):
    sum += A[i]*B[i]

print(sum)
