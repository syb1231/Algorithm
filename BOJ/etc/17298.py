import sys
input = sys.stdin.readline
n = int(input())
info = list(map(int,input().split()))
s = [0]
answer = []
for i in range(len(info)-1,-1,-1):
    val = s[-1]
    if(val<=info[i]):
        s.pop()
        while(s):
            if(s[-1] > info[i]):
                answer.append(s[-1])
                break
            else:
                s.pop()
        if(not s):
            answer.append(-1)

    else:
        answer.append(s[-1])
    s.append(info[i])

for a in range(len(answer)-1,-1,-1):
    print(answer[a],end=" ")
        
