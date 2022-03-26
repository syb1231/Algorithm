import heapq

def solution(operations):
    answer = [0,0]
    heapMax = []
    heapMin = []
    size = 0
    for oper in operations:
        oper = oper.split(' ')
        if(oper[0]=='I'):
            number = int(oper[1])
            heapq.heappush(heapMax, (number*-1,number))
            heapq.heappush(heapMin,number)
            size += 1
        if(oper[0]=='D' and oper[1] == '1' and size):
            heapq.heappop(heapMax)[1] 
            size -= 1
        elif(oper[0]=='D' and oper[1] == '-1' and size ):
            heapq.heappop(heapMin)
            size -= 1
    if(not size):
        return answer
    hashMax = {}
    hashMin = {}
    while(heapMax):
        hashMax[heapq.heappop(heapMax)[1]] = 1

    while(heapMin):
        hashMin[heapq.heappop(heapMin)] = 1

    for value in hashMax:
        if(hashMin.get(value) != None):
            answer[0] = value
            break

    for value in hashMin:
        if(hashMax.get(value) != None):
            answer[1] = value
            break

    return answer
