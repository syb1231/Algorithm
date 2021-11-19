import sys

N = int(sys.stdin.readline()) 
arr = [[0]*2 for _ in range(N)]
for index in range(N):
    a, b = map(int, sys.stdin.readline().split()) 
    arr[index][0], arr[index][1] = a,b

arr.sort(key=lambda x : (x[1], x[0]))

lastTime = -1
count = 0
for index in range(N):
    if(lastTime<=arr[index][0]):
        count += 1
        lastTime = arr[index][1]

print(count)
