import sys
input = sys.stdin.readline
n = int(input())
info = list(map(int,input().split()))
s = [[0,0]]
answer = []
for i in range(len(info)):
    val = s[-1][1]
    if(val<info[i]):
        s.pop()
        while(s):
            if(s[-1][1] > info[i]):
                answer.append(s[-1][0]+1)
                break
            else:
                s.pop()
        if(not s):
            answer.append(0)

    else:
        answer.append(s[-1][0]+1)
    s.append([i,info[i]])

for a in answer:
    print(a,end=" ")
