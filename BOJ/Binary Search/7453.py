import sys
input = sys.stdin.readline

n = int(input())
info = list(map(int,input().split()))

info.sort()
start = 0
end = n-1
answer = []
minVal = float('inf')
while(start<end):
    tmp = info[start] + info[end]

    if(abs(tmp)<minVal):
        minVal = abs(tmp)
        answer = [info[start],info[end]]

    if(tmp<0):
        start +=  1
    else:
        end -=  1

print(answer[0],answer[1])
