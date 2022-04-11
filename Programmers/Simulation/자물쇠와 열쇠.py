def right(key):
    n = len(key)
    newKey = [[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            newKey[y][x] = key[x][n-y-1]
    return newKey

def left(key):
    n = len(key)
    newKey = [[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            newKey[y][x] = key[n-x-1][y]
    return newKey

def cal(newKey,lock,isLockCount):
    m = len(newKey)
    n = len(lock)
    keyArr = []
    for y in range(m):
        for x in range(m):
            if(newKey[y][x]):
                keyArr.append([x,y])     

    for yPlus in range(-m+1,n):
        for xPlus in range(-m+1,n):
            count = 0
            correct = True
            for x,y in keyArr:
                nx = x + xPlus
                ny = y + yPlus
                if(-1<nx<n and -1<ny<n):
                    if(lock[ny][nx]):
                        correct = False
                        break
                    else: 
                        count += 1
                        
            if(count != isLockCount):
                correct = False
            if(correct):
                return True
    
    return False

def solution(key, lock):
    answer = True
    keyLeft90 = left(key)
    key180 = left(keyLeft90)
    keyRight90 = right(key)
    isLockCount = 0

    n = len(lock)
    for y in range(n):
        for x in range(n):
            if(not lock[y][x]):
                isLockCount += 1

                
    if(cal(key,lock,isLockCount) or cal(keyLeft90,lock,isLockCount) or cal(key180,lock,isLockCount) or cal(keyRight90,lock,isLockCount)):
        return True
    return False
