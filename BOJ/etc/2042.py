import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

arr = [0]*(n+1)
tree = [0]*(n+1)

def init(start,end,index):
    if start==end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start+end) // 2
    tree[index] = init(start,mid,index*2) + init(mid + 1, end, index*2 +1)
    return tree[index]

def prefixSum(i):
    result = 0
    while i>0:
        result += tree[i]
        i -= (i&-i)
    return result

def update(i,dif):
    while i<=n:
        tree[i] += dif
        i += (i & -i)

def intervalSum(start,end):
    return prefixSum(end) - prefixSum(start-1)

for i in range(1,n+1):
    x = int(input())
    arr[i] = x
    update(i,x)

for i in range(m+k):
    a,b,c = map(int,input().split())
    if a==1:
        update(b,c-arr[b])
        arr[b] = c
    else:
        print(intervalSum(b,c))
