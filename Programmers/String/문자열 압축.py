def solution(s):
    answer = len(s)
    for size in range(1, len(s)//2 + 1):
        index = 0
        tmp = 1
        nowCount = len(s)
        maxI = len(s) - 2*size + 2
        while(index<len(s)):
            tmp = 0
            if(s[index:index+size] == s[index+size:index+size+size]):
                index += size
                tmp += 2
                while(index<maxI and s[index:index+size] == s[index+size:index+size+size]):
                    tmp += 1
                    index += size
            index += size
            count = 0
            if(tmp):
                nowCount -= (tmp-1) * size
                nowCount += 1
            while(tmp//10):
                count += 1
                tmp = tmp // 10
            nowCount += count 
        answer = min(nowCount,answer)  
    return answer
