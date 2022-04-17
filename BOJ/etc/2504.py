import sys
input = sys.stdin.readline

def divide(tmp):
    if(len(tmp)<3):
        if(tmp[0] == '('):
            return 2
        else:
            return 3
    multiVal = 2
    if(tmp[0] == '['):
        multiVal = 3
    tmp = tmp[1:-1]
    divideTmp = []
    garoCount = 0
    specGaroCount = 0
    index = 0
    for i in range(len(tmp)):
        if(tmp[i]=='('):
            garoCount +=1
        elif(tmp[i]==')'):
            garoCount -= 1
        elif(tmp[i]=='['):
            specGaroCount +=1
        elif(tmp[i]==']'):
            specGaroCount -= 1

        if(not garoCount and not specGaroCount):
            divideTmp.append(tmp[index:i+1])
            index = i+1
    val = 0
    for divideT in divideTmp:
        val += divide(divideT)
    return val*multiVal

info = str(input()[:-1])
literal = ['(',')','[',']']
garoCount = 0
specGaroCount = 0
divideInfo = []
index = 0
for i in range(len(info)):
    if(info[i]=='('):
        garoCount +=1
    elif(info[i]==')'):
        if(info[i-1] == '['):
            print(0)
            exit()
        garoCount -= 1
    elif(info[i]=='['):
        specGaroCount +=1
    elif(info[i]==']'):
        if(info[i-1] == '('):
            print(0)
            exit()
        specGaroCount -= 1
    if(not garoCount and not specGaroCount):
        divideInfo.append(info[index:i+1])
        index = i+1
if(garoCount or specGaroCount):
    print(0)
    exit()
answer = 0
for divideI in divideInfo:
    answer += divide(divideI)
print(answer)
