import sys

def cal(board,startX,startY):
    Color=board[startY][startX]
    if(Color == "W") : Color = "B"
    elif(Color == "B") : Color = "W"
    count = 0
    for y in range(startY,startY+8):
        for x in range(startX,startX+8):    
            if(board[y][x] != Color) :  count += 1
            if(Color == "W") : Color = "B"
            elif(Color == "B") : Color = "W"          
        if(Color == "W") : Color = "B"
        elif(Color == "B") : Color = "W"  
    if(count > 64-count):
        count = 64-count
    return count

N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())

minCount = 987654321

xMin = 0
yMin = 0 
xMax = M-7
yMax = N-7
for y in range(yMax):
    for x in range(xMax):
        val = cal(board,x,y)
        if(minCount>val): minCount = val
            

print(minCount)
