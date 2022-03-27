def solution(distance, rocks, n):
    answer = 0
    start = 0
    end = 1000000000
    rocks.sort()
    while(start<=end):
        mid = (start + end) // 2
        prev = 0
        count = n + 1
        for rock in rocks:
            dist = rock - prev
            if(dist<mid):
                count -= 1
                if(not count):
                    end = mid - 1
                    break
            else:
                prev = rock
        if(count):
            start = mid + 1
            answer = max(answer,mid)

    return answer
  
  # 이진 탐색 유형인줄 몰랐으면 그 방법으로 풀 수 없었을거 같음 문제 많이 풀자
