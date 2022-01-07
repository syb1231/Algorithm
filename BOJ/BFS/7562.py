from collections import deque
import sys
#input = sys.stdin.readline()
dx= [-2,-1,1,2,-2,-1,+1,+2]
dy= [-1,-2,-2,-1,1,2,2,1]
def bfs(startx,starty,endx,endy):
    check = [[-1]*N for _ in range(N)]
    check[starty][startx] = 0
    visted = deque()
    visted.append([startx,starty])
    while visted:
        x,y = visted.popleft()
        if(x == endx and y == endy):
            return check[y][x]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx > -1 and nx < N and ny > -1 and ny < N and check[ny][nx] == -1):
                visted.append([nx,ny])
                check[ny][nx] = check[y][x] + 1


T = int(sys.stdin.readline())


for test_case in range(T):
    N = int(sys.stdin.readline())
    startx, starty = map(int,input().split())
    endx, endy = map(int,input().split())
    print(bfs(startx,starty,endx,endy))


