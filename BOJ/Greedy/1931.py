import sys


N = int(sys.stdin.readline()) 
time = [[0]*2 for _ in range(N)]
for index in range(N):
    a, b = map(int, sys.stdin.readline().split()) 
    time[index][0] = a 
    time[index][1] = b

time.sort(key=lambda x : (x[1], x[0]))

lastTime=-1
count=0
for index in range(N):
    if(lastTime<=time[index][0]):
        count += 1
        lastTime = time[index][1]

print(count)

