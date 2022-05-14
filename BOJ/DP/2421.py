import sys 
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10000)
def dp(a,b):
    if(d[a][b] != -1):
        return d[a][b]
    
    d[a][b] = max(dp(a-1,b) , dp(a,b-1)) +isPrime(int(str(a)+str(b)))
    return d[a][b]

def isPrime(num):
    if(num < 2):
        return 0

    m = int(num**0.5)
    for i in range(2,m+1):
        if(not num%i):
            return 0
    return 1
        

n = int(input())
d = [[-1 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    d[0][i] = 0
    d[i][0] = 0
d[1][1] = 0 


val = 0

print(dp(n,n) - isPrime(int(str(n)+str(n))))
