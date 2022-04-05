def solution(gems):
    check = {}
    for g in gems:
        check[g] = 1
    
    count = len(check)
    twoPointerHash = {}
    start = 0
    end = -1
    for g in gems:
        if(len(twoPointerHash) == count):
            break
        
        if(twoPointerHash.get(g) == None):
            twoPointerHash[g] = 1
        else:   
            twoPointerHash[g] += 1
        end += 1

    while(start<end and twoPointerHash[gems[start]]>1):
        twoPointerHash[gems[start]] -= 1
        start += 1
    answer = [start,end]
    ansCount = end - start

    end += 1
    while(end<len(gems)):
        twoPointerHash[gems[end]] += 1
        while(start<end and twoPointerHash[gems[start]]>1):
            twoPointerHash[gems[start]] -= 1
            start += 1
        if(ansCount>end-start):
            ansCount = end - start
            answer = [start,end]
        end += 1
    answer[0] += 1
    answer[1] += 1
    return answer
